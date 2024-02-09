import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import { API_ENDPOINTS } from '../urls'
import Issue, { type IIssue } from '../components/Issue'

interface IProjectDetails {
  id: number
  name: string
  description: string
  created_by: string
}

const Project = (): React.ReactElement => {
  const { projectId } = useParams<{ projectId: string }>()
  const [project, setProject] = useState<IProjectDetails | null>(null)
  const [issues, setIssues] = useState<IIssue[]>([])

  useEffect(() => {
    const fetchProject = async (): Promise<void> => {
      try {
        if (projectId == null) return
        const response = await fetch(API_ENDPOINTS.PROJECT_DETAIL(projectId), {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
          },
          credentials: 'include',
        })
        if (!response.ok) {
          throw new Error('Failed to fetch project')
        }
        const projectData = await response.json()
        setProject(projectData as IProjectDetails)
      } catch (error) {
        console.error('Error fetching project:', error)
      }
    }
    const fetchIssues = async (): Promise<void> => {
      try {
        if (projectId == null) return
        const response = await fetch(API_ENDPOINTS.PROJECT_ISSUES(projectId), {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
          },
          credentials: 'include',
        })
        if (!response.ok) {
          throw new Error('Failed to fetch issues')
        }
        const issuesData = (await response.json()).results
        setIssues(issuesData as IIssue[])
      } catch (error) {
        console.error('Error fetching issues:', error)
      }
    }

    void fetchProject()
    void fetchIssues()
  }, [projectId])

  if (project == null) {
    return <div>Loading...</div>
  }

  return (
    <div>
      <h2>{project.name}</h2>
      <p>{project.description}</p>
      <p>{project.created_by}</p>
      <h3>Issues</h3>
      <div>
        {issues?.map((issue) => <Issue key={issue.id} issue={issue} />)}
      </div>
    </div>
  )
}

export default Project
