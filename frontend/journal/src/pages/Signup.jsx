import { useState } from "react";
import axios from "axios";


const SignupForm = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const [emailErrors, setEmailErrors] = useState([]);
  const [passwordErrors, setPasswordErrors] = useState([]);

  const handleSubmit = (event) => {
    event.preventDefault();

    {/* handle submission of the form here */}
    const url = "/api/users/account/register/";
    axios.post(url, {
      email: email,
      password: password
    })
    .then(response => {
      console.log(response)
    })
    .catch(error => {
      if (error.response.data.email)
        setEmailErrors(error.response.data.email);
      else if (error.response.data.password)
        setPasswordErrors(error.response.data.password);
    });

    {/* Clear the inputs */}
    setEmail("");
    setPassword("");
  }

  return <>

    <form method="post" onSubmit={handleSubmit}>
      <div>
        <label htmlFor="id_email">Email</label>
        <input
          value={email}
          onChange={e => setEmail(e.target.value)}
          placeholder="Email Address"
          id="id_email"
          type="email"
          name="email"
          required
        />
      </div>
      <div>
        <label htmlFor="id_password">Password</label>
        <input 
          value={password}
          onChange={e => setPassword(e.target.value)}
          placeholder="Password"
          id="id_password"
          type="password"
          name="password"
          required
        />
      </div>
      <button type="submit">Register</button>
    </form>
  </>
}


const SignupPage = () => {
  {/* TODO - 
      write signup logic and make sure it works
    */}

  
  return <>
    <SignupForm />
  </>
};

export default SignupPage;