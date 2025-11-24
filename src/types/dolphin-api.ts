/**
 * Базовые типы Dolphin Anty API
 * Сгенерировано автоматически
 */

export interface Profile {
  id?: number;
  name?: string;
  browser?: string;
  os?: string;
  userAgent?: string;
}

export interface CreateProfileRequest {
  name: string;
  browser: string;
  os?: string;
}

export interface APIResponse<T = any> {
  data?: T;
  error?: string;
  success: boolean;
}
