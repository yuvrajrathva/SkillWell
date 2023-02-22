import logo from './logo.svg';
import './App.css';
import Homepage from "./Homepage.js";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./Navbar.js";

function App() {
  return (
    <>
      <Router>
        <div className="app">
          <Navbar />
          <Routes>
            <Route path="/" element={<Homepage />} />
            {/* <Route path="/*" element={<Error />} /> */}
          </Routes>
        </div>
      </Router>
    </>
  );
}

export default App;
