import { useState, useEffect } from 'react'
import './App.css'
import axios from "axios";

function App() {
  const [people, setPeople] = useState([]);

  useEffect(() => {
    axios.get("/api").then(res => setPeople(res.data));
  }, []);

  return people.map((p, index) => {
    return (
      <p key={index}>{p.id} <b>{p.name}</b> {p.age}</p>
    )
  })
}

export default App
