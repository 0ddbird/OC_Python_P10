const BASE_URL = 'http://localhost:8000/api'

export const API_ENDPOINTS = {
  LOGIN: `${BASE_URL}/login/`,
  REGISTER: `${BASE_URL}/users/create/`,
  PROJECTS: `${BASE_URL}/projects/`,
  PROJECT_DETAIL: (projectId: number | string) =>
    `${BASE_URL}/projects/${projectId}/`,
  ISSUE_CREATE: (projectId: number | string) =>
    `${BASE_URL}/projects/${projectId}/issues/create/`,
  ISSUE_DETAIL: (projectId: number | string, issueId: number | string) =>
    `${BASE_URL}/projects/${projectId}/issues/${issueId}/`,
  COMMENT_CREATE: (projectId: number | string, issueId: number | string) =>
    `${BASE_URL}/projects/${projectId}/issues/${issueId}/comments/`,
  COMMENT_DETAIL: (
    projectId: number | string,
    issueId: number | string,
    commentId: number | string,
  ) =>
    `${BASE_URL}/projects/${projectId}/issues/${issueId}/comments/${commentId}/`,
}
