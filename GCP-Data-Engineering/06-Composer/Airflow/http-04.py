def __init__(self,
             *,
             server: BaseServer.mro,
             http_conn_id: str = 'http_default',  # Reserve
             method: str = 'GET', # Reserve
             endpoint: str,
             data: Optional[Dict] = None,
             env: Optional[Dict[str, str]] = None,
             output_encoding: str = 'utf-8',
             skip_exit_code: int = 99,
             err_exit_code: int = 500,
             check_response_callable: Callable = lambda res: res.get('Success'),
             **kwargs):
    """
    :param server: BaseServer provide url, port.
    :param endpoint: Url endpoint.
    :param data: A dict data for url.
    :param err_exit_code: Raise exception when this code returned.
    :param err_result_callable: Check response by result data.
    """
    data_str = ' '
    if data:
        for k,v in data.items():
            data_str += f'--data-urlencode "{k}={v}" '
    self.bash_command = f'curl -X GET -G -i  http://{server.HOST}:{server.API_PORT}/{endpoint}' + data_str
    super(BashHttpOperator, self).__init__(bash_command=self.bash_command, env=env, output_encoding=output_encoding,  skip_exit_code=skip_exit_code, **kwargs)
    self.err_exit_code = err_exit_code
    self.check_response_callable = check_response_callable

def execute(self, context):
    env = self.get_env(context)
    result = self.subprocess_hook.run_command(
        command=['bash', '-c', self.bash_command],
        env=env,
        output_encoding=self.output_encoding,
    )
    self.log.info(f'------Status code: {result.exit_code}------')
    if self.skip_exit_code is not None and result.exit_code == self.skip_exit_code:
        raise AirflowSkipException(f"Bash command returned exit code {self.skip_exit_code}. Skipping.")
    elif self.err_exit_code and result.exit_code == self.err_exit_code:
        raise Exception('Internal server error, pls check API logs.')
    elif result.exit_code == 56:
        raise Exception(f'Connect to IP failed !!!')
    elif result.exit_code != 0:
        raise Exception('Bash command failed. The command returned a non-zero exit code.')
    res:dict = json.loads(result.output)
    if self.check_response_callable:
        if not self.check_response_callable(res):
            raise Exception(f'Task failed due to param: check_response_callable (check this param and response for detail), response: {res}')
    return res