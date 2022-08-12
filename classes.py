class Television:
    """
    A class representing details of a television object.
    """
    MIN_CHANNEL = 0  # Minimum TV channel
    MAX_CHANNEL = 3  # Maximum TV channel

    MIN_VOLUME = 0  # Minimum TV volume
    MAX_VOLUME = 2  # Maximum TV volume

    def __init__(self) -> None:
        """
        Constructor that creates initial state of a television object.
        """
        self.__channel: int = Television.MIN_CHANNEL
        self.__volume: int = Television.MIN_VOLUME
        self.__on_off: bool = False

    def power(self) -> None:
        """
        Method that is used to change TV status from on to off and from off to on.
        """
        if self.__on_off:
            self.__on_off = False
        else:
            self.__on_off = True

    def channel_up(self) -> None:
        """
        This method helps to go one channel up from the current channel when TV is on.
        """
        if self.__on_off:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        This method helps to go one channel down from the current channel when TV is on.
        """
        if self.__on_off:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        This method helps to volume up TV when TV is on.
        """
        if self.__on_off:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
            else:
                self.__volume = Television.MAX_VOLUME

    def volume_down(self) -> None:
        """
        This method helps to volume down TV when TV is on.
        """
        if self.__on_off:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
            else:
                self.__volume = Television.MIN_VOLUME

    def __str__(self) -> str:
        """
        This method returns a string that helps to know the status of TV, channel and volume
        of a TV object.
        :return: A string
        """
        return f'TV status: Is on = {self.__on_off}, Channel = {self.__channel}, Volume = {self.__volume}'


