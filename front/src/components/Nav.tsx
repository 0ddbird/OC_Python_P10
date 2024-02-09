import React from 'react'
import { Link } from 'react-router-dom'
import { useAuth } from '../contexts/AuthContext'

const Nav = (): React.ReactElement => {
  const { isAuthenticated, logout } = useAuth()

  return (
    <nav className="bg-blue-500 py-4">
      <div className="container mx-auto flex justify-between items-center">
        <h1 className="text-white text-2xl font-bold">SoftDesk</h1>
        <ul className="flex space-x-4">
          {!isAuthenticated ? (
            <>
              <li>
                <Link to="/login" className="text-white hover:underline">
                  Login
                </Link>
              </li>
              <li>
                <Link to="/register" className="text-white hover:underline">
                  Register
                </Link>
              </li>
            </>
          ) : (
            <>
              <li>
                <Link to="/projects" className="text-white hover:underline">
                  Projects
                </Link>
              </li>
              <li>
                <button onClick={logout} className="text-white hover:underline">
                  Logout
                </button>
              </li>
            </>
          )}
        </ul>
      </div>
    </nav>
  )
}

export default Nav
