  // src/services/chatApi.js
  const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000/api';

  class ChatApi {
    getToken() {
      if (typeof window === 'undefined') return null;
      return localStorage.getItem('auth_token');
    }

    async request(endpoint, options = {}) {
      const token = this.getToken();
      const headers = {
        'Content-Type': 'application/json',
        ...(token && { Authorization: `Bearer ${token}` }),
        ...options.headers,
      };

      const response = await fetch(`${API_BASE_URL}${endpoint}`, {
        ...options,
        headers,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return response.json();
    }

    async getUserSessions() {
      return this.request('/conversations');
    }

    async getSessionMessages(conversationId) {
      return this.request(`/conversations/${conversationId}`);
    }

    async processMessage(message, conversationId = null) {
      return this.request('api/chat', {
        method: 'POST',
        body: JSON.stringify({
          message,
          conversation_id: conversationId,
        }),
      });
    }
  }

  const chatApi = new ChatApi();
  export default chatApi;