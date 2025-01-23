import java.util.logging.Level;
import java.util.logging.Logger;

public class LoggingManager {
    private Logger logger;

    public LoggingManager() {
        logger = Logger.getLogger(getClass().getName());
    }

    public void logEvent(Level level, String message) {
        logger.log(level, message);
    }

    public void logError(Level level, String message, Throwable throwable) {
        StackTraceElement[] stackTrace = throwable.getStackTrace();
        StackTraceElement relevantElement = stackTrace[0]; // Top of the stack trace (where the error occurred)

        String detailedMessage = String.format(
                "%s: %s (at %s:%d in %s)",
                message,
                throwable.getMessage(),
                relevantElement.getFileName(),
                relevantElement.getLineNumber(),
                relevantElement.getMethodName()
        );

        logger.log(level, detailedMessage);
    }
}
