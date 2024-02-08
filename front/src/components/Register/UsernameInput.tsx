import React from 'react'

interface IUsernameInputProps {
  username: string
  setUsername: React.Dispatch<React.SetStateAction<string>>
}

const UsernameInput: React.FC<IUsernameInputProps> = ({
  username,
  setUsername,
}): React.ReactElement => {
  return (
    <div>
      <label htmlFor="username" className="sr-only">
        Username
      </label>
      <input
        id="username"
        name="username"
        type="text"
        autoComplete="username"
        required
        className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
        placeholder="Username"
        value={username}
        onChange={(e) => {
          setUsername(e.target.value)
        }}
      />
    </div>
  )
}

export default UsernameInput
