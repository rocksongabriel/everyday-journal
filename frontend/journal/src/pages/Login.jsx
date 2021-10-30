import { useState } from "react";
import axios from "axios";


const LoginForm = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const [errors, setErrors] = useState("");

  const [acessToken, setAccessToken] = useState("");
  const [refreshToken, setRefreshToken] = useState("");


  const handleSubmit = (event) => {
    event.preventDefault();

    {/* handle submission of the form here */}
    const url = "/api/token/";
    axios.post(url, {
      email: email,
      password: password
    })
    .then(response => {
      setAccessToken(response.data.access);
      setRefreshToken(response.data.refresh);
    })
    .catch(error => {
      if (error.response.data) 
        setErrors(error.response.data.detail);
    });

    {/* Clear the inputs */}
    setEmail("");
    setPassword("");
  };

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

const LoginPage = () => {
  return <>
    <LoginForm />
  </>
};

export default LoginPage;