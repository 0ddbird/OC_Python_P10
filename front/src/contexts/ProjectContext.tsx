import React, {
  createContext,
  useContext,
  useState,
  useEffect,
  useCallback,
  type ReactNode,
} from 'react'

export interface IProject {
  id: number
  name: string
  description: string
}

interface ProjectContextType {
  projects: IProject[]
  setProjects: (projects: IProject[]) => void
}

const ProjectContext = createContext<ProjectContextType | null>(null)

export const useProjectContext = (): ProjectContextType => {
  const context = useContext(ProjectContext)
  if (context == null) {
    throw new Error('useProjectContext must be used within a ProjectProvider')
  }
  return context
}

export const ProjectProvider = ({
  children,
}: {
  children: ReactNode
}): React.ReactElement => {
  const [projects, setProjects] = useState<IProject[]>([])

  const updateProjects = useCallback((newProjects: IProject[]) => {
    setProjects(newProjects)
  }, [])

  useEffect(() => {
    const initialProjects: IProject[] = []
    setProjects(initialProjects)
  }, [])

  return (
    <ProjectContext.Provider value={{ projects, setProjects: updateProjects }}>
      {children}
    </ProjectContext.Provider>
  )
}
