export type UserRole = "beginner" | "advanced" | "expert" | "admin" | "developer";

export interface Bot {
  name: string;
  status: "running" | "stopped";
}

export interface Strategy {
  name: string;
  type: "visual" | "ai" | "code";
}