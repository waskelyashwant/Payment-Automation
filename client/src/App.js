import "./App.css";
import { useState } from "react";
import axios from "axios";
import { Button } from "@material-ui/core";
import logo1 from "./bill_file.jpg";
import logo2 from "./card_file.jpg";

function App() {
  const [selectedFile, setSelectedFile] = useState();
  const [selectedFile2, setSelectedFile2] = useState();
  const [isFilePicked, setIsFilePicked] = useState(false);
  const [isFilePicked2, setIsFilePicked2] = useState(false);
  const changeHandler = (e) => {
    setSelectedFile(e.target.files[0]);
    setIsFilePicked(true);
  };
  const changeHandler2 = (e) => {
    setSelectedFile2(e.target.files[0]);
    setIsFilePicked2(true);
  };
  const handleSubmission = () => {
    const data = new FormData();
    data.append("file", selectedFile);
    data.append("file2", selectedFile2);
    axios.post("/sendFile", data).then((res) => {
      alert(res.data.code);
    });
  };
  const runScript = () => {
    fetch("/status")
      .then((res) => res.json())
      .then((data) => {
        if (data.value === 0) alert(data.code);
        else {
          fetch("/runScript")
            .then((res) => res.json())
            .then((data) => {
              alert(data.code);
            });
        }
      });
    // fetch("/runScript")
    //   .then((res) => res.json())
    //   .then((data) => {
    //     alert(data.code);
    //   });
  };
  const stopScript = () => {
    fetch("/stopScript")
      .then((res) => res.json())
      .then((data) => {
        alert(data.code);
      });
  };
  const billCheck = () => {
    fetch("/status2")
      .then((res) => res.json())
      .then((data) => {
        if (data.value === 0) alert(data.code);
        else {
          fetch("/billCheck")
            .then((res) => res.json())
            .then((data) => {
              alert(data.code);
            });
        }
      });
  };
  const stopScript2 = () => {
    fetch("/stopScript2")
      .then((res) => res.json())
      .then((data) => {
        alert(data.code);
      });
  };

  return (
    <div className="App">
      <div className="run">
        <Button variant="outlined" color="primary" onClick={billCheck}>
          Bill Check
        </Button>
        <span> </span>
        <Button variant="outlined" color="secondary" onClick={stopScript2}>
          Stop Bill Check
        </Button>
      </div>
      <div>
        <h3>Bill excel file should have same column name as given below.</h3>
        <img src={logo1} alt="bill file format"></img>
      </div>
      <div className="d-flex">
        <h4>
          Select Bill Details ( Excel File (
          <span style={{ color: "red" }}> .xlsx</span> format) )
        </h4>
        <input
          className="input"
          type="file"
          name="file"
          placeholder="Bill Details (Excel File))"
          onChange={changeHandler}
        />
        {isFilePicked ? (
          <div>
            <p>Filename: {selectedFile.name}</p>
          </div>
        ) : (
          <p>Select a file to show details</p>
        )}
      </div>
      <br></br>
      <div>
        <h3>
          Card details excel file should have same column name as given below.
        </h3>
        <img src={logo2} alt="Card details file format"></img>
        <div className="d-flex">
          <h4>
            {" "}
            Select Card Details ( Excel File (
            <span style={{ color: "red" }}> .xlsx</span> format) )
          </h4>
          <input
            className="input"
            type="file"
            name="file"
            placeholder="Bill Details (Excel File))"
            onChange={changeHandler2}
          />
          {isFilePicked2 ? (
            <div>
              <p>Filename: {selectedFile2.name}</p>
              {/* <p>Filetype: {selectedFile2.type}</p> */}
            </div>
          ) : (
            <p>Select a file to show details</p>
          )}
        </div>
      </div>
      <div>
        {selectedFile && selectedFile2 && (
          <Button variant="outlined" color="primary" onClick={handleSubmission}>
            Upload Files
          </Button>
        )}
      </div>
      <div className="run">
        <Button variant="outlined" color="primary" onClick={runScript}>
          Run Script
        </Button>
      </div>
      <div style={{ marginTop: "10px" }}>
        <Button variant="outlined" color="secondary" onClick={stopScript}>
          Stop Script
        </Button>
      </div>
    </div>
  );
}

export default App;
