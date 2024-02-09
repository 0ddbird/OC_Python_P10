import * as React from 'react'

const canDataBeSharedCheckbox = (): React.ReactElement => {
  return (
    <div>
      <label htmlFor="canDataBeShared" className="flex items-center space-x-2">
        <input
          id="canDataBeShared"
          name="canDataBeShared"
          type="checkbox"
          className="h-4 w-4 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded"
        />
        <span>I accept to share my data</span>
      </label>
    </div>
  )
}

export default canDataBeSharedCheckbox
