from robber.expect import expect
from robber.matchers.base import Base

class RespondTo(Base):
    def matches(self):
        return hasattr(self.actual, self.expected) \
               and callable(getattr(self.actual, self.expected))

    def failure_message(self):
        return 'Expected "%s" to respond to "%s"' % (self.actual, self.expected)

expect.register('respond_to', RespondTo)