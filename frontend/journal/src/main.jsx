import React from 'react'
import ReactDOM from 'react-dom'
import './css/index.css'
import App from './App'
import axios from "axios";

// axios config
axios.defaults.baseURL = "http://localhost:8000";


ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
)
