import React, { useEffect, useState } from 'react'
import useRegister from '../hooks/useRegister'
import UsernameInput from '../components/inputs/UsernameInput'
import PasswordInput from '../components/inputs/PasswordInput'
import BirthdateInput from '../components/inputs/BirthDateInput'
import CanBeContactedCheckbox from '../components/inputs/CanBeContactedCheckbox'
import CanDataBeSharedCheckbox from '../components/inputs/CanDataBeSharedCheckbox'
import EmailInput from '../components/inputs/EmailInput'
import { useNavigate } from 'react-router-dom'

const RegisterForm = (): React.ReactElement => {
  const { register, isLoading, error, isSuccess } = useRegister()
  const navigate = useNavigate()
  console.log(error)
  const [username, setUsername] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [birthdate, setBirthdate] = useState('')

  useEffect(() => {
    if (isSuccess) {
      navigate('/projects')
    }
  }, [isSuccess, navigate])

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>): void => {
    event.preventDefault()

    const canBeContacted = (
      event.currentTarget.elements.namedItem(
        'canBeContacted',
      ) as HTMLInputElement
    ).checked
    const canDataBeShared = (
      event.currentTarget.elements.namedItem(
        'canDataBeShared',
      ) as HTMLInputElement
    ).checked

    void (async () => {
      try {
        await register({
          username,
          email,
          password,
          birthdate,
          canBeContacted,
          canDataBeShared,
        })
      } catch (error) {
        console.error('Registration failed:', error)
      }
    })()
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <div className="max-w-md w-full space-y-8 p-10 bg-white shadow rounded-lg">
        <div>
          <h2 className="mt-6 text-center text-3xl font-extrabold text-gray-900">
            Register
          </h2>
        </div>
        <form className="mt-8 space-y-6" onSubmit={handleSubmit}>
          <div className="rounded-md shadow-sm -space-y-px">
            <UsernameInput username={username} setUsername={setUsername} />
            <EmailInput email={email} setEmail={setEmail} />
            <PasswordInput password={password} setPassword={setPassword} />
            <BirthdateInput birthdate={birthdate} setBirthdate={setBirthdate} />
            <CanBeContactedCheckbox />
            <CanDataBeSharedCheckbox />
          </div>
          <div>
            <button
              type="submit"
              disabled={isLoading}
              className="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
            >
              {isLoading ? 'Registering...' : 'Register'}
            </button>
          </div>
        </form>
      </div>
    </div>
  )
}

export default RegisterForm
