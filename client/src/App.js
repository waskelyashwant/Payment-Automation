import "./App.css";
import { useState } from "react";
import axios from "axios";
import { Button } from "@material-ui/core";
import logo1 from "./bill_file.jpg";
import logo2 from "./card_file.jpg";
import file from "./results/Bill File updated.csv";

function App() {
  let flag = 0;
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
  const [value, setValue] = useState(null);
  const [print, setPrint] = useState(false);

  function handleChange(e) {
    setValue(e.target.value);
    setPrint(false);
    flag = 0;
  }

  const handleSubmit = () => {
    flag = 1;
    const data = new FormData();
    data.append("value", value);
    setPrint(true);
    console.log(value);
    axios
      .post("/sendAppValue", data)
      .then((res) => {
        // alert(res.data.code);
        console.log(res);
      })
      .catch((error) => {
        console.log(error);
      });

    // or you can send data to backend
  };

  const handleKeyPress = (e) => {
    // console.log("hello");
    // //it triggers by pressing the enter key
    // console.log(e.keyCode);
    if (e.keyCode === 13) {
      alert("success");
      handleSubmit();
    }
  };

  const runScript = () => {
    if (value === null) {
      alert("Total number of apps field cannot be empty");
      return false;
    } else if (flag == 0) {
      handleSubmit();
    }
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

  function download() {
    // alert("Hello");
    window.open("http://127.0.0.1:8887/Bill%20File%20updated.csv", "_blank");
  }

  const getAppNo = () => {
    fetch("/appNo")
      .then((res) => res.json())
      .then((data) => {
        let text =
          "Currently running :-\nBiller name = " +
          String(data.bN) +
          "\nK number = " +
          String(data.kN) +
          "\nApp number = " +
          String(data.aN);
        alert(text);
      });
  };

  const delFile = () => {
    fetch("/delFile")
      .then((res) => res.json())
      .then((data) => {
        if (data.value === 1) {
          alert("File successfully deleted");
        } else {
          alert("No such file");
        }
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
        <a href="http://127.0.0.1:5000/" target="_blank">
          Bill check link
        </a>
      </div>
      <div className="container my-4">
        <div className="row">
          <div className="col border border-secondary">
            <div>
              <h5>
                Bill excel file should have same column name as given below.
              </h5>
              <img src={logo1} alt="bill file format"></img>
            </div>
            <div className="d-flex">
              <h6>
                Select Bill Details ( Excel File (
                <span style={{ color: "red" }}> .xlsx</span> format) )
              </h6>
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
          </div>
          <div className="col border border-secondary">
            <div>
              <h5>
                Card details excel file should have same column name as given
                below.
              </h5>
              <img src={logo2} alt="Card details file format"></img>
              <div className="d-flex">
                <h6>
                  {" "}
                  Select Card Details ( Excel File (
                  <span style={{ color: "red" }}> .xlsx</span> format) )
                </h6>
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
          </div>
        </div>
      </div>

      <div>
        {selectedFile && selectedFile2 && (
          <Button variant="outlined" color="primary" onClick={handleSubmission}>
            Upload Files
          </Button>
        )}
      </div>

      <p>Total number of apps in your device</p>
      <input
        className="app_no"
        type="number"
        placeholder="totalApps"
        onChange={handleChange}
        onKeyPress={handleKeyPress}
      />
      <button onClick={handleSubmit} type="submit" className="appbut">
        Submit
      </button>
      {print ? (
        <p>Total number of apps in your device are {value}</p>
      ) : (
        <p>Please choose total number of apps</p>
      )}

      <div className="run">
        <p className="war">!! Make sure to start the appium server !!</p>
        <Button variant="outlined" color="primary" onClick={runScript}>
          Run Script
        </Button>
        <span>&emsp;</span>
        <Button variant="outlined" color="secondary" onClick={stopScript}>
          Stop Script
        </Button>
      </div>
      <div>
        <br></br>
        <button className="del" onClick={delFile}>
          Delete old bill status file
        </button>
        <span>&emsp;</span>
        <button variant="contained" color="default" onClick={download}>
          Download Bill
        </button>
        <span>&emsp;</span>
        <button variant="contained" className="app" onClick={getAppNo}>
          App processing
        </button>
      </div>
    </div>
  );
}

export default App;
