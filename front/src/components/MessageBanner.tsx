import * as React from 'react'
import { useMessage } from '../contexts/MessageContext'
import { useEffect, useState } from 'react'

const MessageBanner = (): React.ReactElement | null => {
  const { message } = useMessage()
  const [isVisible, setIsVisible] = useState(true)

  useEffect(() => {
    if (message != null && message !== '') {
      setIsVisible(true)
    }
  }, [message])

  const handleClose = (): void => {
    setIsVisible(false)
  }

  if (message == null || message === '' || !isVisible) return null

  return (
    <div className="bg-red-600 text-white py-2">
      <span>{message}</span>
      <button
        onClick={handleClose}
        className="text-white mr-4"
        aria-label="Close message"
      >
        &#x2715;
      </button>
    </div>
  )
}

export default MessageBanner
