import React from 'react'
import { Navigate } from 'react-router-dom'
import { useAuth } from '../contexts/AuthContext'

interface PrivateRouteProps {
  component: React.ComponentType
}

const PrivateRoute = ({
  component: Component,
}: PrivateRouteProps): React.ReactElement => {
  const { isAuthenticated } = useAuth()

  return isAuthenticated ? <Component /> : <Navigate to="/login" />
}

export default PrivateRoute
