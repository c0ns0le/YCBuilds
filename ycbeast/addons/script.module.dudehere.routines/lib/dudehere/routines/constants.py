from dudehere.routines import *

WINDOWXML = enum(
	ALIGN_LEFT = 0,
	ALIGN_RIGHT = 1,
	ALIGN_CENTER_X = 2,
	ALIGN_CENTER_Y = 4,
	ALIGN_CENTER = 6,
	ALIGN_TRUNCATED = 8,
	ALIGN_JUSTIFY = 10,
	MESSAGE_ACTION_OK = 110,
	MESSAGE_EXIT = 111
)

WINDOW_ACTIONS = enum(
	ACTION_PREVIOUS_MENU = 10,
	ACTION_NAV_BACK = 92,
	ACTION_MOVE_LEFT = 1,
	ACTION_MOVE_RIGHT = 2,
	ACTION_MOVE_UP = 3,
	ACTION_MOVE_DOWN = 4,
	ACTION_MOUSE_WHEEL_UP = 104,
	ACTION_MOUSE_WHEEL_DOWN = 105,
	ACTION_MOUSE_DRAG = 106,
	ACTION_MOUSE_MOVE = 107,
	ACTION_MOUSE_LEFT_CLICK = 100,
	ACTION_ENTER = 13,
	ACTION_SELECT_ITEM = 7,
	ACTION_MOUSE_RIGHT_CLICK = 101,
	ACTION_SHOW_INFO = 11,
	ACTION_CONTEXT_MENU = 117,
)