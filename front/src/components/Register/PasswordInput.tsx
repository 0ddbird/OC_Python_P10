import React from 'react'

interface IPasswordInputProps {
  password: string
  setPassword: React.Dispatch<React.SetStateAction<string>>
}

const PasswordInput: React.FC<IPasswordInputProps> = ({
  password,
  setPassword,
}): React.ReactElement => {
  return (
    <div>
      <label htmlFor="password" className="sr-only">
        Password
      </label>
      <input
        id="password"
        name="password"
        type="password"
        autoComplete="new-password"
        required
        className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
        placeholder="Password"
        value={password}
        onChange={(e) => {
          setPassword(e.target.value)
        }}
      />
    </div>
  )
}

export default PasswordInput
