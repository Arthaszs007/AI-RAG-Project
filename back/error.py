class BaseAppError(Exception):
    def __init__(self, message:str,stage:str = "unknow",retryable:bool= False):
        super().__init__(message)
        self.message = message
        self.stage = stage
        self.retryable = retryable

class ParserError(BaseAppError):
    def __init__(self, message = "Parser Failed", stage = "Parser", retryable = False):
        super().__init__(message, stage, retryable)

class SplitError(BaseAppError):
    def __init__(self, message="Split Failed", stage = "Split", retryable = False):
        super().__init__(message, stage, retryable)

class EmbeddingError(BaseAppError):
    def __init__(self, message="Embedding Failed", stage = "Embedding", retryable = False):
        super().__init__(message, stage, retryable)

class RetrieveError(BaseAppError):
    def __init__(self, message="Retrieve Failed", stage = "Retrieve", retryable = False):
        super().__init__(message, stage, retryable)
