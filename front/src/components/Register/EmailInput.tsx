import React from 'react'

interface IEmailInputProps {
  email: string
  setEmail: React.Dispatch<React.SetStateAction<string>>
}

const EmailInput: React.FC<IEmailInputProps> = ({
  email,
  setEmail,
}): React.ReactElement => {
  return (
    <div>
      <label htmlFor="email" className="sr-only">
        Email
      </label>
      <input
        id="email"
        name="email"
        type="text"
        autoComplete="email"
        required
        className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
        placeholder="email"
        value={email}
        onChange={(e) => {
          setEmail(e.target.value)
        }}
      />
    </div>
  )
}

export default EmailInput
