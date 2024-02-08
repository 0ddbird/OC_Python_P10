import * as React from 'react'

const canBeContactedCheckbox = (): React.ReactElement => {
  return (
    <div>
      <label htmlFor="canBeContacted" className="flex items-center space-x-2">
        <input
          id="canBeContacted"
          name="canBeContacted"
          type="checkbox"
          className="h-4 w-4 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded"
        />
        <span>Can be contacted?</span>
      </label>
    </div>
  )
}

export default canBeContactedCheckbox
