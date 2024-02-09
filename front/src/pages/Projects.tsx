import React, { useEffect, useState } from 'react'
import ProjectTile from '../components/ProjectTile'
import { type IProject } from '../interfaces'
import { API_ENDPOINTS } from '../urls'

const Projects = (): React.ReactElement => {
  const [projects, setProjects] = useState<IProject[]>([])

  useEffect(() => {
    const fetchProjects = async (): Promise<void> => {
      const response = await fetch(API_ENDPOINTS.PROJECTS, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
        credentials: 'include',
      })
      const projects = (await response.json()).results as IProject[]
      setProjects(projects)
    }

    void fetchProjects()
  }, [])

  return (
    <div>
      <h2 className="text-2xl font-bold mb-4">Projects</h2>
      <div className="grid grid-cols-1 gap-4">
        {projects.map((project) => (
          <div key={project.id}>
            <ProjectTile project={project} />
          </div>
        ))}
      </div>
    </div>
  )
}

export default Projects
