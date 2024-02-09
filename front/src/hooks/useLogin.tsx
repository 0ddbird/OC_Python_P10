import { useState } from 'react'
import { API_ENDPOINTS } from '../urls'

interface ILoginParams {
  username: string
  password: string
}

interface ILoginHookReturn {
  isLoading: boolean
  error: string
  login: (params: ILoginParams) => Promise<void>
  isSuccess: boolean
}

const useLogin = (): ILoginHookReturn => {
  const [isLoading, setIsLoading] = useState(false)
  const [isSuccess, setIsSuccess] = useState(false)
  const [error, setError] = useState('')

  const login = async ({ username, password }: ILoginParams): Promise<void> => {
    setIsLoading(true)
    try {
      const response = await fetch(API_ENDPOINTS.LOGIN, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password }),
      })
      if (!response.ok) {
        throw new Error('Login failed')
      }
      setIsSuccess(true)
    } catch (error) {
      setError(error instanceof Error ? error.message : String(error))
    } finally {
      setIsLoading(false)
    }
  }

  return { login, isLoading, error, isSuccess }
}

export default useLogin
