import { useState } from 'react';
import React from 'react';
export default function Form() {
  /*Defining the hooks to use function/ change variable values
  without classes*/ 
    const [name, setFirstName] = useState('');
    const [email, setText] = useState('');
    const [message, setMessage] = useState('');
    const[optradio, setOptRadio] = useState('');

    /*This function, handles the change of values in case the users select
    different buttons*/

    const onOptionChange = e => {
      setOptRadio(e.target.value)
    }

  /*This function prints the contents given in the form, on clicking the submit button*/
  const handleSubmit = (e) => {
    e.preventDefault();
    var n = name.toUpperCase();
    setMessage(` Hello UCE ${n}, your mail is ${email} and your tower is ${optradio}`);
   // setFirstName('');
   // setText('');
  }
    // to add submit logic 
  return (
    <form onSubmit={handleSubmit}>
        <h2>Enter UCE Details</h2>
        <div className="form-group">
        <label>Enter your 521 ID</label>
        <input
          type="text"
          className="form-control"
          id="ID"
          name="ID"
          placeholder="BHATTAD5"
          onChange={(e) =>
            setFirstName(e.target.value)
          }
          
        />
      </div>
      <div className="form-group">
        <label for="UCEMail">Enter your Novartis mail ID </label>
        <input
          type="email"
          className="form-control"
          id="UCEMail"
          name="UCEMail"
          placeholder="aditya.bhattacharjee@novartis.net"
          onChange={(e) =>
            setText(e.target.value)
          }
        />
      </div>
      <h3> Enter tower details</h3>
      <label className="radio-inline">
      <input type="radio" name="optradio" id="radio" value="NTO"onChange={onOptionChange} />NTO
    </label>
    <label className="radio-inline">
      <input type="radio" name="optradio" id="radio" value="Commericial" onChange={onOptionChange} />COM
    </label>
    <label className="radio-inline">
      <input type="radio" name="optradio" id="radio" value="GDD" onChange={onOptionChange}/>GDD
    </label>
    <label classNameName="radio-inline">
      <input type="radio" name="optradio" id="radio" value="CBS" onChange={onOptionChange}/>CBS
    </label><br/>
    <input class="btn btn-primary" type="submit" value="Submit"onChange={onOptionChange}/>
    <p>{message}</p>
    </form>
  );
}
