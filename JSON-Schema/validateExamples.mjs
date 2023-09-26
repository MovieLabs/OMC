import { readdirSync, readFileSync } from 'fs';
import Ajv2019 from "ajv/dist/2019.js";

const schema = JSON.parse(readFileSync("./omc/omc-v2.0.schema-2019.json", {encoding: "utf8"}));
const ajv = new Ajv2019({allowUnionTypes: true, verbose: true});
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

