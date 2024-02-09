import React from 'react'

export interface IIssue {
  id: number
  title: string
  description: string
  status: string
  priority: string
  tag: string
  assigned_to: string | null
  created_by: string
  created_at: string
  updated_at: string
}

const Issue: React.FC<{ issue: IIssue }> = ({ issue }) => {
  return (
    <div className="border border-gray-200 p-4 rounded-md shadow-md">
      <h3 className="text-lg font-bold mb-2">{issue.title}</h3>
      <p className="text-gray-600 mb-2">{issue.description}</p>
      <div className="flex justify-between items-center">
        <div>
          <p>
            <span className="font-bold">Status:</span> {issue.status}
          </p>
          <p>
            <span className="font-bold">Priority:</span> {issue.priority}
          </p>
          <p>
            <span className="font-bold">Tag:</span> {issue.tag}
          </p>
          <p>
            <span className="font-bold">Assigned to:</span>{' '}
            {issue.assigned_to != null || 'Unassigned'}
          </p>
          <p>
            <span className="font-bold">Created by:</span> {issue.created_by}
          </p>
          <p>
            <span className="font-bold">Created at:</span>{' '}
            {new Date(issue.created_at).toLocaleString()}
          </p>
          <p>
            <span className="font-bold">Updated at:</span>{' '}
            {new Date(issue.updated_at).toLocaleString()}
          </p>
        </div>
      </div>
    </div>
  )
}

export default Issue
