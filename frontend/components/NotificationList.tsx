import React, { useState, useEffect } from "react";

interface Notification {
  id: number;
  message: string;
  type: string;
  is_read: boolean;
  created_at: string;
}

export default function NotificationList() {
  const [notifications, setNotifications] = useState<Notification[]>([]);
  const [showNotifications, setShowNotifications] = useState(false);

  useEffect(() => {
    const fetchNotifications = async () => {
      try {
        const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/notifications`, {
          headers: {
            'Authorization': 'Bearer YOUR_AUTH_TOKEN' // Replace with actual token
          }
        });
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data: Notification[] = await response.json();
        setNotifications(data);
      } catch (error) {
        console.error("Error fetching notifications:", error);
      }
    };
    fetchNotifications();
  }, []);

  const unreadCount = notifications.filter(n => !n.is_read).length;

  return (
    <div className="relative">
      <button onClick={() => setShowNotifications(!showNotifications)} className="relative">
        {unreadCount > 0 && (
          <span className="absolute -top-1 -right-1 w-4 h-4 bg-red-500 text-white text-xs rounded-full flex items-center justify-center">
            {unreadCount}
          </span>
        )}
        <svg className="w-6 h-6 text-neon-magenta" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V4a2 2 0 10-4 0v1.341C7.67 7.165 6 9.388 6 12v2.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" />
        </svg>
      </button>

      {showNotifications && (
        <div className="absolute right-0 mt-2 w-80 bg-glass rounded-xl shadow-neon-magenta backdrop-blur-xs p-4 z-10">
          <h3 className="text-lg font-semibold text-neon-magenta mb-2">Notifications</h3>
          {notifications.length === 0 ? (
            <p className="text-gray-400">No new notifications.</p>
          ) : (
            <ul>
              {notifications.map((notification) => (
                <li key={notification.id} className={`p-2 rounded mb-2 ${notification.is_read ? "bg-gray-800" : "bg-gray-700"}`}>
                  <p className="text-sm">{notification.message}</p>
                  <span className="text-xs text-gray-400">{new Date(notification.created_at).toLocaleString()}</span>
                </li>
              ))}
            </ul>
          )}
        </div>
      )}
    </div>
  );
}