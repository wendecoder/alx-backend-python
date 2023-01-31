#!/usr/bin/env python3
"""
Test For Client Module
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
import client


class TestGithubOrgClient(unittest.TestCase):
    """ Class for testing client module """

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch("client.get_json")
    def test_org(self, org, mk_get_json):
        """ Test Org property"""

        gc = client.GithubOrgClient(org)
        url = gc.ORG_URL.format(org=org)
        gc.org()
        mk_get_json.assert_called_once_with(url)

    def test_public_repos_url(self):
        """ test property"""
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as my_org:
            my_org.return_value = {"repos_url": "www.google.com"}
            gc = client.GithubOrgClient("google")
            self.assertEqual(gc._public_repos_url, "www.google.com")

    @patch("client.get_json")
    def test_public_repos(self, mock_json):
        """ Test public_repos """
        mock_json.return_value = [{'license': {'key': 'apache-2.0',
                                               'name': 'Apache License 2.0',
                                               'node_id': 'MDc6TGljZW5zZTI=',
                                               'spdx_id': 'Apache-2.0'},
                                   'name': 'truth'
                                   },
                                  {
            'license': None,
            'name': 'ruby-openid-apps-discovery'
        },
            {
                'license': {'key': 'apache-2.0',
                            'name': 'Apache License 2.0',
                            'node_id': 'MDc6TGljZW5zZTI=',
                            'spdx_id': 'Apache-2.0',
                            },
                'name': 'autoparse'
        },
            {
                                      'license': {'key': 'other',
                                                  'name': 'Other',
                                                  'node_id': 'MDc6TG=',
                                                  'spdx_id': 'NOASSERTION',
                                                  'url': None},

                                      'name': 'anvil-build'}
        ]
        with patch("client.GithubOrgClient._public_repos_url"
                   ) as mock_repo_url:
            mock_repo_url.return_value = "https://api.google.com/repos"
            gc = client.GithubOrgClient("google")
            gc._public_repos_url()
            self.assertEqual(gc.public_repos(), [
                             'truth',
                             'ruby-openid-apps-discovery',
                             'autoparse', 'anvil-build'])
            self.assertEqual(gc.public_repos("other"), ['anvil-build'])
            mock_json.assert_called_once()
            mock_repo_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, lic, out):
        """ test has license """
        self.assertEqual(client.GithubOrgClient.has_license(repo, lic), out)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Class for Integration test of fixtures """

    @classmethod
    def setUpClass(cls):
        """A class method called before tests in an individual class are run"""

        config = {'return_value.json.side_effect':
                  [
                      cls.org_payload, cls.repos_payload,
                      cls.org_payload, cls.repos_payload
                  ]
                  }
        cls.get_patcher = patch('requests.get', **config)

        cls.mock = cls.get_patcher.start()

    def test_public_repos(self):
        """ Integration test: public repos"""
        test_class = GithubOrgClient("google")

        self.assertEqual(test_class.org, self.org_payload)
        self.assertEqual(test_class.repos_payload, self.repos_payload)
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """ Integration test for public repos with License """
        test_class = GithubOrgClient("google")

        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.assertEqual(test_class.public_repos(
            "apache-2.0"), self.apache2_repos)
        self.mock.assert_called()

    @classmethod
    def tearDownClass(cls):
        """A class method called after tests in an individual class have run"""
        cls.get_patcher.stop()
