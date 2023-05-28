
import "./App.css";
import NavBar from "./Custom-Components/NavBar";
import Form from "./Custom-Components/Form";

function App() { // function calls of Navbar and Form as seen here
  return (
    <>
      <NavBar/> 
    <div className="container-sm">
      <Form/>
    </div>
    </>
  );
}

export default App;
