import { useState } from 'react'
import { API_ENDPOINTS } from '../urls'

interface IRegisterParams {
  username: string
  email: string
  password: string
  birthdate: string
  canBeContacted: boolean
  canDataBeShared: boolean
}

interface IRegisterHookReturn {
  isLoading: boolean
  error: string
  register: (params: IRegisterParams) => Promise<void>
  isSuccess: boolean
}

const useRegister = (): IRegisterHookReturn => {
  const [isSuccess, setIsSuccess] = useState(false)
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState('')

  const register = async ({
    username,
    email,
    password,
    birthdate,
    canBeContacted,
    canDataBeShared,
  }: IRegisterParams): Promise<void> => {
    setIsLoading(true)
    try {
      const response = await fetch(API_ENDPOINTS.REGISTER, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          username,
          email,
          password,
          birthdate,
          can_be_contacted: canBeContacted,
          can_data_be_shared: canDataBeShared,
        }),
      })

      if (!response.ok) {
        throw new Error('Signup failed')
      }
      setIsSuccess(true)
    } catch (error) {
      setError(error instanceof Error ? error.message : String(error))
    } finally {
      setIsLoading(false)
    }
  }

  return { register, isLoading, error, isSuccess }
}

export default useRegister
