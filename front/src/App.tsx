import React from 'react'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import LoginForm from './pages/LoginForm'
import RegisterForm from './pages/RegisterForm'
import Projects from './pages/Projects'
import { AuthProvider } from './contexts/AuthContext'
import Nav from './components/Nav'
import { MessageProvider } from './contexts/MessageContext'
import MessageBanner from './components/MessageBanner'
import Home from './pages/Home'
import PrivateRoute from './components/PrivateRoute'
import Project from './pages/Project'

const App = (): React.ReactElement => {
  return (
    <MessageProvider>
      <AuthProvider>
        <Router>
          <div className="app-container">
            <Nav />
            <MessageBanner />
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/login" element={<LoginForm />} />
              <Route path="/register" element={<RegisterForm />} />
              <Route
                path="/projects"
                element={<PrivateRoute component={Projects} />}
              />
              <Route
                path="/projects/:projectId"
                element={<PrivateRoute component={Project} />}
              />
            </Routes>
          </div>
        </Router>
      </AuthProvider>
    </MessageProvider>
  )
}

export default App
