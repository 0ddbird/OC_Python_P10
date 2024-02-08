import { useState } from 'react'

interface ILoginHookReturn {
  isLoading: boolean
  error: string
  login: (username: string, password: string) => Promise<void>
}

const useLogin = (): ILoginHookReturn => {
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState('')

  const login = async (username: string, password: string): Promise<void> => {
    setIsLoading(true)
    try {
      const response = await fetch('/api/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password }),
      })
      if (!response.ok) {
        throw new Error('Login failed')
      }
      const data = await response.json()
      console.log(data)
    } catch (error) {
      setError(error instanceof Error ? error.message : String(error))
    } finally {
      setIsLoading(false)
    }
  }

  return { login, isLoading, error }
}
