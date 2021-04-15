import docker
from docker.errors import APIError

import logging

import pytest


LOGGER = logging.getLogger(__name__)


@pytest.mark.parametrize(
    'language,version_output', [('python', ['Python', '3.8.9\n']),],
)
def test_python_version(language, version_output):
    """Ensure that the language is available in the container's PATH and that
    it has the correct version
    """
    LOGGER.info(f'Test that language {language} is correctly installed ...')
    client = docker.from_env()
    output = client.containers.run('illumidesk/grader-setup-service:latest', f'{language} --version')
    output_decoded = output.decode('utf-8').split(' ')
    assert output_decoded[0:3] == version_output
    LOGGER.info(f'Output from command: {output_decoded[0:3]}')


def test_invalid_cmd():
    """Ensure that an invalid command returns a docker.errors.ContainerError
    """
    with pytest.raises(APIError):
        LOGGER.info('Test an invalid command ...')
        client = docker.from_env()
        client.containers.run('illumidesk/grader-setup-service:latest', 'foo --version')
