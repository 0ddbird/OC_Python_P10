import React, { useEffect, useState } from 'react'
import UsernameInput from '../components/inputs/UsernameInput'
import PasswordInput from '../components/inputs/PasswordInput'
import { useNavigate } from 'react-router-dom'
import useLogin from '../hooks/useLogin'

const LoginForm = (): React.ReactElement => {
  const { login, isLoading, error, isSuccess } = useLogin()
  console.log(error)
  const navigate = useNavigate()
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')

  useEffect(() => {
    if (isSuccess) {
      navigate('/projects')
    }
  }, [isSuccess, navigate])

  const handleSubmit = (event: React.FormEvent): void => {
    event.preventDefault()
    void (async () => {
      try {
        await login({
          username,
          password,
        })
      } catch (error) {
        console.error('Login failed:', error)
      }
    })()
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <div className="max-w-md w-full space-y-8 p-10 bg-white shadow rounded-lg">
        <div>
          <h2 className="mt-6 text-center text-3xl font-extrabold text-gray-900">
            Login
          </h2>
        </div>
        <form className="mt-8 space-y-6" onSubmit={handleSubmit}>
          <input type="hidden" name="remember" defaultValue="true" />
          <div className="rounded-md shadow-sm -space-y-px">
            <UsernameInput username={username} setUsername={setUsername} />
            <PasswordInput password={password} setPassword={setPassword} />
          </div>

          <div>
            <button
              type="submit"
              disabled={isLoading}
              className="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
            >
              {isLoading ? 'Logging in...' : 'Login'}
            </button>
          </div>
        </form>
      </div>
    </div>
  )
}

export default LoginForm
