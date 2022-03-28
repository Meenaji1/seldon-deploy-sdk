# coding: utf-8

"""
    Seldon Deploy API

    API to interact and manage the lifecycle of your machine learning models deployed through Seldon Deploy.  # noqa: E501

    OpenAPI spec version: v1alpha1
    Contact: hello@seldon.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from seldon_deploy_sdk.api_client import ApiClient


class SecretsServiceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def secrets_service_create_gcs_bucket_secret(self, namespace, remote, body, **kwargs):  # noqa: E501
        """Creates a GCS bucket secret according to specified parameters.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.secrets_service_create_gcs_bucket_secret(namespace, remote, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str namespace: The namespace to create secret in. (required)
        :param str remote: The name of the remote to create, can be lowercase characters or numbers up to 10 characters long. The created secret will be named {remote}-bucket. (required)
        :param object body: The GCS account credentials to populate the secret. See documentation for how to generate this. (required)
        :return: V1CreateGCSBucketSecretResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.secrets_service_create_gcs_bucket_secret_with_http_info(namespace, remote, body, **kwargs)  # noqa: E501
        else:
            (data) = self.secrets_service_create_gcs_bucket_secret_with_http_info(namespace, remote, body, **kwargs)  # noqa: E501
            return data

    def secrets_service_create_gcs_bucket_secret_with_http_info(self, namespace, remote, body, **kwargs):  # noqa: E501
        """Creates a GCS bucket secret according to specified parameters.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.secrets_service_create_gcs_bucket_secret_with_http_info(namespace, remote, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str namespace: The namespace to create secret in. (required)
        :param str remote: The name of the remote to create, can be lowercase characters or numbers up to 10 characters long. The created secret will be named {remote}-bucket. (required)
        :param object body: The GCS account credentials to populate the secret. See documentation for how to generate this. (required)
        :return: V1CreateGCSBucketSecretResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['namespace', 'remote', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method secrets_service_create_gcs_bucket_secret" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `secrets_service_create_gcs_bucket_secret`")  # noqa: E501
        # verify the required parameter 'remote' is set
        if ('remote' not in params or
                params['remote'] is None):
            raise ValueError("Missing the required parameter `remote` when calling `secrets_service_create_gcs_bucket_secret`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `secrets_service_create_gcs_bucket_secret`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'namespace' in params:
            path_params['namespace'] = params['namespace']  # noqa: E501
        if 'remote' in params:
            path_params['remote'] = params['remote']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/secrets/{namespace}/bucket/gcs/{remote}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1CreateGCSBucketSecretResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def secrets_service_create_rclone_bucket_secret(self, namespace, remote, body, **kwargs):  # noqa: E501
        """Creates a generic rclone bucket secret according to specified parameters.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.secrets_service_create_rclone_bucket_secret(namespace, remote, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str namespace: The namespace to create secret in. (required)
        :param str remote: The name of the remote to create, can be lowercase characters or numbers up to 10 characters long. The created secret will be named {remote}-bucket. (required)
        :param V1RcloneConfig body: The rclone key value pairs. (required)
        :return: V1CreateRcloneBucketSecretResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.secrets_service_create_rclone_bucket_secret_with_http_info(namespace, remote, body, **kwargs)  # noqa: E501
        else:
            (data) = self.secrets_service_create_rclone_bucket_secret_with_http_info(namespace, remote, body, **kwargs)  # noqa: E501
            return data

    def secrets_service_create_rclone_bucket_secret_with_http_info(self, namespace, remote, body, **kwargs):  # noqa: E501
        """Creates a generic rclone bucket secret according to specified parameters.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.secrets_service_create_rclone_bucket_secret_with_http_info(namespace, remote, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str namespace: The namespace to create secret in. (required)
        :param str remote: The name of the remote to create, can be lowercase characters or numbers up to 10 characters long. The created secret will be named {remote}-bucket. (required)
        :param V1RcloneConfig body: The rclone key value pairs. (required)
        :return: V1CreateRcloneBucketSecretResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['namespace', 'remote', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method secrets_service_create_rclone_bucket_secret" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `secrets_service_create_rclone_bucket_secret`")  # noqa: E501
        # verify the required parameter 'remote' is set
        if ('remote' not in params or
                params['remote'] is None):
            raise ValueError("Missing the required parameter `remote` when calling `secrets_service_create_rclone_bucket_secret`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `secrets_service_create_rclone_bucket_secret`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'namespace' in params:
            path_params['namespace'] = params['namespace']  # noqa: E501
        if 'remote' in params:
            path_params['remote'] = params['remote']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/secrets/{namespace}/bucket/rclone/{remote}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1CreateRcloneBucketSecretResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def secrets_service_create_registry_secret(self, namespace, name, body, **kwargs):  # noqa: E501
        """Creates a registry secret according to specified parameters.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.secrets_service_create_registry_secret(namespace, name, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str namespace: The namespace to create secret in. (required)
        :param str name: The name of the secret to create. (required)
        :param object body: The raw json docker credentials config. (required)
        :return: V1CreateRegistrySecretResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.secrets_service_create_registry_secret_with_http_info(namespace, name, body, **kwargs)  # noqa: E501
        else:
            (data) = self.secrets_service_create_registry_secret_with_http_info(namespace, name, body, **kwargs)  # noqa: E501
            return data

    def secrets_service_create_registry_secret_with_http_info(self, namespace, name, body, **kwargs):  # noqa: E501
        """Creates a registry secret according to specified parameters.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.secrets_service_create_registry_secret_with_http_info(namespace, name, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str namespace: The namespace to create secret in. (required)
        :param str name: The name of the secret to create. (required)
        :param object body: The raw json docker credentials config. (required)
        :return: V1CreateRegistrySecretResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['namespace', 'name', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method secrets_service_create_registry_secret" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `secrets_service_create_registry_secret`")  # noqa: E501
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `secrets_service_create_registry_secret`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `secrets_service_create_registry_secret`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'namespace' in params:
            path_params['namespace'] = params['namespace']  # noqa: E501
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/secrets/{namespace}/registry/{name}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1CreateRegistrySecretResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def secrets_service_create_s3_bucket_secret(self, namespace, remote, body, **kwargs):  # noqa: E501
        """Creates a S3 bucket secret according to specified parameters.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.secrets_service_create_s3_bucket_secret(namespace, remote, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str namespace: The namespace to create secret in. (required)
        :param str remote: The name of the remote to create, can be lowercase characters or numbers up to 10 characters long. The created secret will be named {remote}-bucket. (required)
        :param V1S3Credentials body: The S3 account credentials to populate the secret. See documentation for how to generate these. (required)
        :return: V1CreateS3BucketSecretResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.secrets_service_create_s3_bucket_secret_with_http_info(namespace, remote, body, **kwargs)  # noqa: E501
        else:
            (data) = self.secrets_service_create_s3_bucket_secret_with_http_info(namespace, remote, body, **kwargs)  # noqa: E501
            return data

    def secrets_service_create_s3_bucket_secret_with_http_info(self, namespace, remote, body, **kwargs):  # noqa: E501
        """Creates a S3 bucket secret according to specified parameters.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.secrets_service_create_s3_bucket_secret_with_http_info(namespace, remote, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str namespace: The namespace to create secret in. (required)
        :param str remote: The name of the remote to create, can be lowercase characters or numbers up to 10 characters long. The created secret will be named {remote}-bucket. (required)
        :param V1S3Credentials body: The S3 account credentials to populate the secret. See documentation for how to generate these. (required)
        :return: V1CreateS3BucketSecretResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['namespace', 'remote', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method secrets_service_create_s3_bucket_secret" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `secrets_service_create_s3_bucket_secret`")  # noqa: E501
        # verify the required parameter 'remote' is set
        if ('remote' not in params or
                params['remote'] is None):
            raise ValueError("Missing the required parameter `remote` when calling `secrets_service_create_s3_bucket_secret`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `secrets_service_create_s3_bucket_secret`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'namespace' in params:
            path_params['namespace'] = params['namespace']  # noqa: E501
        if 'remote' in params:
            path_params['remote'] = params['remote']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/secrets/{namespace}/bucket/s3/{remote}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1CreateS3BucketSecretResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def secrets_service_delete_secret(self, namespace, secret_type, name, **kwargs):  # noqa: E501
        """Deletes the specified secret.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.secrets_service_delete_secret(namespace, secret_type, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str namespace: The namespace to delete secret from. (required)
        :param str secret_type: The secret type of the secret to be deleted, can be one of (`bucket`, `registry`). (required)
        :param str name: The name of the secret to delete. (required)
        :return: V1DeleteSecretResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.secrets_service_delete_secret_with_http_info(namespace, secret_type, name, **kwargs)  # noqa: E501
        else:
            (data) = self.secrets_service_delete_secret_with_http_info(namespace, secret_type, name, **kwargs)  # noqa: E501
            return data

    def secrets_service_delete_secret_with_http_info(self, namespace, secret_type, name, **kwargs):  # noqa: E501
        """Deletes the specified secret.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.secrets_service_delete_secret_with_http_info(namespace, secret_type, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str namespace: The namespace to delete secret from. (required)
        :param str secret_type: The secret type of the secret to be deleted, can be one of (`bucket`, `registry`). (required)
        :param str name: The name of the secret to delete. (required)
        :return: V1DeleteSecretResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['namespace', 'secret_type', 'name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method secrets_service_delete_secret" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `secrets_service_delete_secret`")  # noqa: E501
        # verify the required parameter 'secret_type' is set
        if ('secret_type' not in params or
                params['secret_type'] is None):
            raise ValueError("Missing the required parameter `secret_type` when calling `secrets_service_delete_secret`")  # noqa: E501
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `secrets_service_delete_secret`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'namespace' in params:
            path_params['namespace'] = params['namespace']  # noqa: E501
        if 'secret_type' in params:
            path_params['secretType'] = params['secret_type']  # noqa: E501
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/secrets/{namespace}/{secretType}/{name}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1DeleteSecretResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def secrets_service_list_secrets(self, namespace, secret_type, **kwargs):  # noqa: E501
        """Lists the names and metadata of secrets used by Seldon Deploy.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.secrets_service_list_secrets(namespace, secret_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str namespace: The namespace to list secrets in. (required)
        :param str secret_type: The secret type, can be one of (`bucket`, `registry`) or `all` to list all secrets used by Seldon Deploy. (required)
        :return: V1ListSecretsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.secrets_service_list_secrets_with_http_info(namespace, secret_type, **kwargs)  # noqa: E501
        else:
            (data) = self.secrets_service_list_secrets_with_http_info(namespace, secret_type, **kwargs)  # noqa: E501
            return data

    def secrets_service_list_secrets_with_http_info(self, namespace, secret_type, **kwargs):  # noqa: E501
        """Lists the names and metadata of secrets used by Seldon Deploy.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.secrets_service_list_secrets_with_http_info(namespace, secret_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str namespace: The namespace to list secrets in. (required)
        :param str secret_type: The secret type, can be one of (`bucket`, `registry`) or `all` to list all secrets used by Seldon Deploy. (required)
        :return: V1ListSecretsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['namespace', 'secret_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method secrets_service_list_secrets" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `secrets_service_list_secrets`")  # noqa: E501
        # verify the required parameter 'secret_type' is set
        if ('secret_type' not in params or
                params['secret_type'] is None):
            raise ValueError("Missing the required parameter `secret_type` when calling `secrets_service_list_secrets`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'namespace' in params:
            path_params['namespace'] = params['namespace']  # noqa: E501
        if 'secret_type' in params:
            path_params['secretType'] = params['secret_type']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/secrets/{namespace}/{secretType}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1ListSecretsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
