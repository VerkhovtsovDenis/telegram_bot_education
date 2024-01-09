from aiogram.filters.state import State, StatesGroup


class FSMClient(StatesGroup):
    waiting_main = State()


class FSMInfo(StatesGroup):
    waiting_info = State()


class FSMApplication(StatesGroup):
    waiting_application = State()


class FSMOrganisation(StatesGroup):
    waiting_organisation = State()
    waiting_organisation_name = State()
    waiting_organisation_type = State()


class FSMUser(StatesGroup):
    waiting_user = State()
    waiting_user_name = State()
    waiting_user_lname = State()
    waiting_user_email = State()
    waiting_user_phone = State()


class FSMEvent(StatesGroup):
    waiting_event = State()
    waiting_event_title = State()
    waiting_event_type = State()
    waiting_event_sdate = State()
    waiting_event_edate = State()


class FSMTs(StatesGroup):
    waiting_ts = State()
    waiting_ts_place = State()
    waiting_ts_sound = State()
    waiting_ts_other = State()

