import React from 'react'
import { Link } from 'react-router-dom'
import { type IProject } from '../interfaces'

interface IProjectProps {
  project: IProject
}

const ProjectTile = ({ project }: IProjectProps): React.ReactElement => {
  return (
    <Link
      to={`/projects/${project.id}/`}
      className="block rounded-md shadow-md hover:shadow-lg"
    >
      <div className="p-4 bg-white">
        <h3 className="text-lg font-bold mb-2 truncate">{project.name}</h3>
        <p className="text-gray-600">{project.description}</p>
      </div>
    </Link>
  )
}

export default ProjectTile
