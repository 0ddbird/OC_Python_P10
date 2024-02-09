import React, {
  createContext,
  useContext,
  useState,
  type ReactNode,
} from 'react'

interface AuthContextType {
  isAuthenticated: boolean
  login: () => void
  logout: () => void
}

const AuthContext = createContext<AuthContextType | null>(null)

export const useAuth = (): AuthContextType => {
  const context = useContext(AuthContext)
  if (context == null) {
    throw new Error('useAuth must be used within an AuthProvider')
  }
  return context
}

export const AuthProvider = ({
  children,
}: {
  children: ReactNode
}): React.ReactElement => {
  const [isAuthenticated, setIsAuthenticated] = useState(false)

  const login = (): void => {
    setIsAuthenticated(true)
  }
  const logout = (): void => {
    setIsAuthenticated(false)
  }

  return (
    <AuthContext.Provider value={{ isAuthenticated, login, logout }}>
      {children}
    </AuthContext.Provider>
  )
}
