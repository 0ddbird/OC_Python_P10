import React from 'react'
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom'
import LoginForm from './components/LoginForm'
import RegisterForm from './components/Register/RegisterForm'

const App = (): React.ReactElement => {
  return (
    <Router>
      <div className="app-container">
        <nav>
          <ul className="flex space-x-4">
            <li>
              <Link to="/login">Login</Link>
            </li>
            <li>
              <Link to="/register">Register</Link>
            </li>
          </ul>
        </nav>
        <Routes>
          <Route path="/login" element={<LoginForm />} />
          <Route path="/register" element={<RegisterForm />} />
        </Routes>
      </div>
    </Router>
  )
}

export default App
