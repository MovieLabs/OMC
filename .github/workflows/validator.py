import asyncio
import http.client
import argparse
import json
from pathlib import Path
from typing import Dict, List, Tuple
from asyncio import Semaphore


class JSONValidator:
    def __init__(self, validator_url: str, max_concurrent: int = 5):
        self.semaphore = Semaphore(max_concurrent)
        network = validator_url.split("://")[1].split("/")[0]
        secure = validator_url.startswith("https://")
        host = network.split(":")[0] if ":" in network else network
        port = 443 if secure else 80
        port = network.split(":")[1] if ":" in network else port
        self.conn = (
            http.client.HTTPSConnection(host=host, port=port)
            if secure
            else http.client.HTTPConnection(host=host, port=port)
        )

    async def validate_file(self, file_path: Path) -> List[str]:
        """Validate a single JSON file and return a list of violated rules"""
        async with self.semaphore:
            try:
                # Prepare the file for upload
                boundary = "----WebKitFormBoundary7MA4YWxkTrZu0gW"
                headers = {"Content-type": f"multipart/form-data; boundary={boundary}"}

                # Read file content
                with open(file_path, "rb") as f:
                    file_content = f.read()

                # Create multipart form data
                body = (
                    (
                        f"--{boundary}\r\n"
                        f'Content-Disposition: form-data; name="file"; filename="{file_path.name}"\r\n'
                        f"Content-Type: application/json\r\n\r\n"
                    ).encode("utf-8")
                    + file_content
                    + (f"\r\n--{boundary}--\r\n").encode("utf-8")
                )

                # Make the POST request
                self.conn.request("POST", "/api/check", body, headers)
                response = self.conn.getresponse()

                if response.status != 200:
                    raise Exception(f"HTTP error: {response.status}")

                result = json.loads(response.read().decode())

                # Return all violated rules
                return self.get_violated_rules(result)

            except Exception as e:
                raise Exception(f"Error processing file: {str(e)}")

    def get_violated_rules(self, result: Dict) -> List[str]:
        """Extract all violated rules from the validation result"""
        return [
            rule
            for rule, issues in result["details"]["issues"].items()
            if len(issues) > 0
        ]

    async def process_directory(
        self, directory: str
    ) -> Tuple[Dict[str, List[str]], Dict[str, List[str]]]:
        """Process all JSON files in the directory and its subdirectories"""
        # Find all JSON files
        path = Path(directory)
        json_files = list(path.rglob("*.json"))

        if not json_files:
            return {}

        # Create validation tasks
        tasks = [self.validate_file(file) for file in json_files]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        # Process results to handle exceptions
        processed_results = {}
        processed_failures = {}
        for file, result in zip(json_files, results):
            if isinstance(result, Exception):
                processed_failures[str(file)] = [str(result)]
            else:
                processed_results[str(file)] = result

        return processed_results, processed_failures

    def error_rules(self, spec: Dict) -> List[str]:
        return [
            rule
            for category in spec["rules"].keys()
            for rule in spec["rules"][category].keys()
            if spec["rules"][category][rule][0] == "error"
        ]

    async def get_spec(self) -> Dict:
        self.conn.request("GET", "/api/spec")
        response = self.conn.getresponse()
        return json.loads(response.read().decode())


def main():
    parser = argparse.ArgumentParser(description="Validate JSON files in a directory")
    parser.add_argument(
        "--base-url",
        type=str,
        default="http://localhost:8000/",
        help="Base URL of the validation service",
    )
    parser.add_argument("--directory", help="Directory containing JSON files")
    parser.add_argument(
        "--max-concurrent",
        type=int,
        default=5,
        help="Maximum number of concurrent validation requests",
    )
    parser.add_argument(
        "--only-errors",
        action="store_true",
        help="Return only files with errors",
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-p",
        action="store_true",
        help="Process the directory and validate JSON files",
    )
    group.add_argument(
        "-s",
        action="store_true",
        help="Return the spec from the validation service",
    )
    args = parser.parse_args()

    # Create validator instance
    validator = JSONValidator(
        validator_url=args.base_url, max_concurrent=args.max_concurrent
    )

    spec = asyncio.run(validator.get_spec())

    if args.s:
        # Return the spec
        print(json.dumps(spec, indent=2))
        exit(0)
    elif args.p:
        # Process the directory
        error_rules = validator.error_rules(spec)
        results, failures = asyncio.run(validator.process_directory(args.directory))
    else:
        # Print help message if no valid command is provided
        parser.print_help()
        exit(1)

    if args.only_errors:
        # Exit with appropriate status code for only errors
        error_files = [
            file
            for file, violations in results.items()
            if any(rule in error_rules for rule in violations)
        ]
        if error_files or failures:
            validated_files = {file: results[file] for file in error_files}
            validated_files = {
                key: [rule for rule in value if rule in error_rules]
                for key, value in validated_files.items()
            }
            print(
                json.dumps(
                    {
                        "status": f"found errors when processing {args.directory}",
                        "validated_files": validated_files,
                        "failed_files": failures,
                    },
                    indent=2,
                )
            )
            exit(1)
        else:
            print(
                json.dumps(
                    {"status": f"no validation errors in {args.directory}"}, indent=2
                )
            )
            exit(0)
    else:
        # Include status and print all violations
        output = {
            "status": f"validation completed for {args.directory}",
            "validated_files": results,
            "failed_files": failures,
        }
        print(json.dumps(output, indent=2))
        exit(0)


if __name__ == "__main__":
    main()
