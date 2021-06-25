const express = require("express");
const app = express();
const port = 5000;
const router = express.Router();
const bodyParser = require("body-parser");
const cors = require("cors");
const fileupload = require("express-fileupload");
const fs = require("fs");
const path = require("path");
app.use(fileupload());
app.use(express.static("files"));
app.use(cors());
app.post("/sendFile", function (req, res) {
  const data = req.files.file;
  fs.writeFile(
    __dirname + "/script/data.xlsx",
    data.data,
    "ascii",
    function (err) {
      if (err) return console.log(err);
    }
  );
  const data2 = req.files.file2;
  fs.writeFile(
    __dirname + "/script/data2.xlsx",
    data2.data,
    "ascii",
    function (err) {
      if (err) return console.log(err);
    }
  );
  res.send({ code: "Success" });
  return;
});

let pythonProcess = null;
let pythonProcess2 = null;
let ended = 1;
let ended2 = 1;
app.get("/runScript", (req, res) => {
  const spawn = require("child_process").spawn;
  pythonProcess = spawn("python", ["./script/script.py"]);
  ended = 0;
  // pythonProcess.kill();
  pythonProcess.stdout.on("data", (data) => {
    console.log(`${data}`);
  });
  pythonProcess.stderr.on("data", (data) => {
    console.error(`stderr: ${data}`);
  });
  pythonProcess.on("close", (code) => {
    ended = 1;
    pythonProcess = null;
    res.send({ code: "Scripted execution done" });
  });
  // res.send({code:"Scripted execution done"});
});
app.get("/status", (req, res) => {
  if (ended === 0)
    res.send({
      code: "Script is already running , Stop before running again .",
      value: 0,
    });
  else res.send({ value: 1 });
});
app.get("/stopScript", (req, res) => {
  if (pythonProcess != null) {
    pythonProcess.kill();
    res.send({ code: "Automation script stopped" });
    pythonProcess = null;
  } else {
    res.send({ code: "Automation script not running" });
  }
});
app.get("/billCheck", (req, res) => {
  const spawn = require("child_process").spawn;
  pythonProcess2 = spawn("python", ["./script/flask/env/app.py"]);
  ended2 = 0;
  // pythonProcess.kill();
  pythonProcess2.stdout.on("data", (data) => {
    console.log(`${data}`);
  });
  pythonProcess2.stderr.on("data", (data) => {
    console.error(`stderr: ${data}`);
  });
  pythonProcess2.on("close", (code) => {
    ended2 = 1;
    pythonProcess2 = null;
    res.send({ code: "Bill check execution done" });
  });
  // res.send({code:"Scripted execution done"});
});
app.get("/stopScript2", (req, res) => {
  if (pythonProcess2 != null) {
    pythonProcess2.kill();
    res.send({ code: "Script stopped" });
    console.log("Bill check stopped");
    pythonProcess2 = null;
  } else {
    res.send({ code: "Script not running" });
    console.log("Bill check not running");
  }
});
app.get("/status2", (req, res) => {
  if (ended2 === 0)
    res.send({
      code: "Bill check is already running , Stop before running again .",
      value: 0,
    });
  else res.send({ value: 1 });
});

app.use(express.static(path.resolve(__dirname, "./client/build")));

app.get("*", (req, res) => {
  res.sendFile(path.resolve(__dirname, "./client/build", "index.html"));
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});
