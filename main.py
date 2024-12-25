import os
import base64


def main():
    code = base64.b64decode(os.getenv("FUNCTION_CODE",base64.b64encode(b"print(\"no function code was found\")")))
    functionName = os.getenv("FUNCTION_NAME")
    functionArguments = os.getenv("FUNCTION_ARGUMENTS", "test")
    args = [a.strip() for a in functionArguments.split(",")]
    namespace = {}
    exec(code, namespace[functionName](args))

if __name__=="__main__":
    main()

