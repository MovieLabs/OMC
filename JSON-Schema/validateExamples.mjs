import { readdirSync, readFileSync } from 'fs';
import Ajv from "ajv";
import addFormats from "ajv-formats";


const schema = JSON.parse(readFileSync("./omc/omc-v0.1.schema.json", {encoding: "utf8"}));
const ajv = new Ajv({strict: "log", "verbose": true});
addFormats(ajv);
const validateOMC = ajv.compile(schema);

const exampleFileNames = readdirSync("./Examples");
for (const exampleFN of exampleFileNames) {
    console.log(exampleFN);
    const example = JSON.parse(readFileSync(`./Examples/${exampleFN}`));
    const valid = validateOMC(example);
    if (!valid) {
        console.log("INVALID:");
        console.log(validateOMC.errors);
    } else {
        console.log("VALID");
    }
    console.log("");
}

