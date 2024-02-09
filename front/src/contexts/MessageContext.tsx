import React, {
  createContext,
  useContext,
  useState,
  type ReactNode,
} from 'react'

interface MessageContextType {
  message: string | null
  setMessage: (message: string | null) => void
}

const MessageContext = createContext<MessageContextType | null>(null)

export const useMessage = (): MessageContextType => {
  const context = useContext(MessageContext)
  if (context == null) {
    throw new Error('useMessage must be used within a MessageProvider')
  }
  return context
}

export const MessageProvider = ({
  children,
}: {
  children: ReactNode
}): React.ReactElement => {
  const [message, setMessage] = useState<string | null>(null)

  return (
    <MessageContext.Provider value={{ message, setMessage }}>
      {children}
    </MessageContext.Provider>
  )
}
