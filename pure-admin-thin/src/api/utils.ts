export const baseUrlApi = (url: string) =>
  process.env.NODE_ENV === "development"
    ? `http://127.0.0.1:3000/${url}`
    : `http://127.0.0.1:3000/${url}`;

export const baseUrlApiParam = (url: string, param) =>
  process.env.NODE_ENV === "development"
    ? `http://127.0.0.1:3000/${url}/${param}`
    : `http://127.0.0.1:3000/${url}/${param}`;
