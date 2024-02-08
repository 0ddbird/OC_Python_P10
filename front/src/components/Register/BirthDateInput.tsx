import React from 'react'

interface IBirthdateInputProps {
  birthdate: string
  setBirthdate: React.Dispatch<React.SetStateAction<string>>
}

const BirthdateInput: React.FC<IBirthdateInputProps> = ({
  birthdate,
  setBirthdate,
}): React.ReactElement => {
  return (
    <div>
      <label htmlFor="birthdate" className="sr-only">
        Birthdate
      </label>
      <input
        id="birthdate"
        name="birthdate"
        type="date"
        required
        className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
        value={birthdate}
        onChange={(e) => {
          setBirthdate(e.target.value)
        }}
      />
    </div>
  )
}

export default BirthdateInput
