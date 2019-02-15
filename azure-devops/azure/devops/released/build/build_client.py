﻿# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from ...v4_1.build import models


class BuildClient(Client):
    """Build
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(BuildClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '965220d5-5bb9-42cf-8d67-9b146df2a5a4'

    def create_artifact(self, artifact, build_id, project=None):
        """CreateArtifact.
        Associates an artifact with a build.
        :param :class:`<BuildArtifact> <azure.devops.v4_1.build.models.BuildArtifact>` artifact: The artifact.
        :param int build_id: The ID of the build.
        :param str project: Project ID or project name
        :rtype: :class:`<BuildArtifact> <azure.devops.v4_1.build.models.BuildArtifact>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        content = self._serialize.body(artifact, 'BuildArtifact')
        response = self._send(http_method='POST',
                              location_id='1db06c96-014e-44e1-ac91-90b2d4b3e984',
                              version='4.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('BuildArtifact', response)

    def get_artifact(self, build_id, artifact_name, project=None):
        """GetArtifact.
        Gets a specific artifact for a build.
        :param int build_id: The ID of the build.
        :param str artifact_name: The name of the artifact.
        :param str project: Project ID or project name
        :rtype: :class:`<BuildArtifact> <azure.devops.v4_1.build.models.BuildArtifact>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        query_parameters = {}
        if artifact_name is not None:
            query_parameters['artifactName'] = self._serialize.query('artifact_name', artifact_name, 'str')
        response = self._send(http_method='GET',
                              location_id='1db06c96-014e-44e1-ac91-90b2d4b3e984',
                              version='4.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('BuildArtifact', response)

    def get_artifact_content_zip(self, build_id, artifact_name, project=None, **kwargs):
        """GetArtifactContentZip.
        Gets a specific artifact for a build.
        :param int build_id: The ID of the build.
        :param str artifact_name: The name of the artifact.
        :param str project: Project ID or project name
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        query_parameters = {}
        if artifact_name is not None:
            query_parameters['artifactName'] = self._serialize.query('artifact_name', artifact_name, 'str')
        response = self._send(http_method='GET',
                              location_id='1db06c96-014e-44e1-ac91-90b2d4b3e984',
                              version='4.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='application/zip')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_artifacts(self, build_id, project=None):
        """GetArtifacts.
        Gets all artifacts for a build.
        :param int build_id: The ID of the build.
        :param str project: Project ID or project name
        :rtype: [BuildArtifact]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        response = self._send(http_method='GET',
                              location_id='1db06c96-014e-44e1-ac91-90b2d4b3e984',
                              version='4.1',
                              route_values=route_values)
        return self._deserialize('[BuildArtifact]', self._unwrap_collection(response))

    def get_badge(self, project, definition_id, branch_name=None):
        """GetBadge.
        Gets a badge that indicates the status of the most recent build for a definition.
        :param str project: The project ID or name.
        :param int definition_id: The ID of the definition.
        :param str branch_name: The name of the branch.
        :rtype: str
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if definition_id is not None:
            route_values['definitionId'] = self._serialize.url('definition_id', definition_id, 'int')
        query_parameters = {}
        if branch_name is not None:
            query_parameters['branchName'] = self._serialize.query('branch_name', branch_name, 'str')
        response = self._send(http_method='GET',
                              location_id='de6a4df8-22cd-44ee-af2d-39f6aa7a4261',
                              version='4.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('str', response)

    def delete_build(self, build_id, project=None):
        """DeleteBuild.
        Deletes a build.
        :param int build_id: The ID of the build.
        :param str project: Project ID or project name
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        self._send(http_method='DELETE',
                   location_id='0cd358e1-9217-4d94-8269-1c1ee6f93dcf',
                   version='4.1',
                   route_values=route_values)

    def get_build(self, build_id, project=None, property_filters=None):
        """GetBuild.
        Gets a build
        :param int build_id:
        :param str project: Project ID or project name
        :param str property_filters:
        :rtype: :class:`<Build> <azure.devops.v4_1.build.models.Build>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        query_parameters = {}
        if property_filters is not None:
            query_parameters['propertyFilters'] = self._serialize.query('property_filters', property_filters, 'str')
        response = self._send(http_method='GET',
                              location_id='0cd358e1-9217-4d94-8269-1c1ee6f93dcf',
                              version='4.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('Build', response)

    def get_builds(self, project=None, definitions=None, queues=None, build_number=None, min_time=None, max_time=None, requested_for=None, reason_filter=None, status_filter=None, result_filter=None, tag_filters=None, properties=None, top=None, continuation_token=None, max_builds_per_definition=None, deleted_filter=None, query_order=None, branch_name=None, build_ids=None, repository_id=None, repository_type=None):
        """GetBuilds.
        Gets a list of builds.
        :param str project: Project ID or project name
        :param [int] definitions: A comma-delimited list of definition IDs. If specified, filters to builds for these definitions.
        :param [int] queues: A comma-delimited list of queue IDs. If specified, filters to builds that ran against these queues.
        :param str build_number: If specified, filters to builds that match this build number. Append * to do a prefix search.
        :param datetime min_time: If specified, filters to builds that finished/started/queued after this date based on the queryOrder specified.
        :param datetime max_time: If specified, filters to builds that finished/started/queued before this date based on the queryOrder specified.
        :param str requested_for: If specified, filters to builds requested for the specified user.
        :param str reason_filter: If specified, filters to builds that match this reason.
        :param str status_filter: If specified, filters to builds that match this status.
        :param str result_filter: If specified, filters to builds that match this result.
        :param [str] tag_filters: A comma-delimited list of tags. If specified, filters to builds that have the specified tags.
        :param [str] properties: A comma-delimited list of properties to retrieve.
        :param int top: The maximum number of builds to return.
        :param str continuation_token: A continuation token, returned by a previous call to this method, that can be used to return the next set of builds.
        :param int max_builds_per_definition: The maximum number of builds to return per definition.
        :param str deleted_filter: Indicates whether to exclude, include, or only return deleted builds.
        :param str query_order: The order in which builds should be returned.
        :param str branch_name: If specified, filters to builds that built branches that built this branch.
        :param [int] build_ids: A comma-delimited list that specifies the IDs of builds to retrieve.
        :param str repository_id: If specified, filters to builds that built from this repository.
        :param str repository_type: If specified, filters to builds that built from repositories of this type.
        :rtype: [Build]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if definitions is not None:
            definitions = ",".join(map(str, definitions))
            query_parameters['definitions'] = self._serialize.query('definitions', definitions, 'str')
        if queues is not None:
            queues = ",".join(map(str, queues))
            query_parameters['queues'] = self._serialize.query('queues', queues, 'str')
        if build_number is not None:
            query_parameters['buildNumber'] = self._serialize.query('build_number', build_number, 'str')
        if min_time is not None:
            query_parameters['minTime'] = self._serialize.query('min_time', min_time, 'iso-8601')
        if max_time is not None:
            query_parameters['maxTime'] = self._serialize.query('max_time', max_time, 'iso-8601')
        if requested_for is not None:
            query_parameters['requestedFor'] = self._serialize.query('requested_for', requested_for, 'str')
        if reason_filter is not None:
            query_parameters['reasonFilter'] = self._serialize.query('reason_filter', reason_filter, 'str')
        if status_filter is not None:
            query_parameters['statusFilter'] = self._serialize.query('status_filter', status_filter, 'str')
        if result_filter is not None:
            query_parameters['resultFilter'] = self._serialize.query('result_filter', result_filter, 'str')
        if tag_filters is not None:
            tag_filters = ",".join(tag_filters)
            query_parameters['tagFilters'] = self._serialize.query('tag_filters', tag_filters, 'str')
        if properties is not None:
            properties = ",".join(properties)
            query_parameters['properties'] = self._serialize.query('properties', properties, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if max_builds_per_definition is not None:
            query_parameters['maxBuildsPerDefinition'] = self._serialize.query('max_builds_per_definition', max_builds_per_definition, 'int')
        if deleted_filter is not None:
            query_parameters['deletedFilter'] = self._serialize.query('deleted_filter', deleted_filter, 'str')
        if query_order is not None:
            query_parameters['queryOrder'] = self._serialize.query('query_order', query_order, 'str')
        if branch_name is not None:
            query_parameters['branchName'] = self._serialize.query('branch_name', branch_name, 'str')
        if build_ids is not None:
            build_ids = ",".join(map(str, build_ids))
            query_parameters['buildIds'] = self._serialize.query('build_ids', build_ids, 'str')
        if repository_id is not None:
            query_parameters['repositoryId'] = self._serialize.query('repository_id', repository_id, 'str')
        if repository_type is not None:
            query_parameters['repositoryType'] = self._serialize.query('repository_type', repository_type, 'str')
        response = self._send(http_method='GET',
                              location_id='0cd358e1-9217-4d94-8269-1c1ee6f93dcf',
                              version='4.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[Build]', self._unwrap_collection(response))

    def queue_build(self, build, project=None, ignore_warnings=None, check_in_ticket=None):
        """QueueBuild.
        Queues a build
        :param :class:`<Build> <azure.devops.v4_1.build.models.Build>` build:
        :param str project: Project ID or project name
        :param bool ignore_warnings:
        :param str check_in_ticket:
        :rtype: :class:`<Build> <azure.devops.v4_1.build.models.Build>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if ignore_warnings is not None:
            query_parameters['ignoreWarnings'] = self._serialize.query('ignore_warnings', ignore_warnings, 'bool')
        if check_in_ticket is not None:
            query_parameters['checkInTicket'] = self._serialize.query('check_in_ticket', check_in_ticket, 'str')
        content = self._serialize.body(build, 'Build')
        response = self._send(http_method='POST',
                              location_id='0cd358e1-9217-4d94-8269-1c1ee6f93dcf',
                              version='4.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('Build', response)

    def update_build(self, build, build_id, project=None):
        """UpdateBuild.
        Updates a build.
        :param :class:`<Build> <azure.devops.v4_1.build.models.Build>` build: The build.
        :param int build_id: The ID of the build.
        :param str project: Project ID or project name
        :rtype: :class:`<Build> <azure.devops.v4_1.build.models.Build>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        content = self._serialize.body(build, 'Build')
        response = self._send(http_method='PATCH',
                              location_id='0cd358e1-9217-4d94-8269-1c1ee6f93dcf',
                              version='4.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Build', response)

    def update_builds(self, builds, project=None):
        """UpdateBuilds.
        Updates multiple builds.
        :param [Build] builds: The builds to update.
        :param str project: Project ID or project name
        :rtype: [Build]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(builds, '[Build]')
        response = self._send(http_method='PATCH',
                              location_id='0cd358e1-9217-4d94-8269-1c1ee6f93dcf',
                              version='4.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[Build]', self._unwrap_collection(response))

    def get_build_changes(self, project, build_id, continuation_token=None, top=None, include_source_change=None):
        """GetBuildChanges.
        Gets the changes associated with a build
        :param str project: Project ID or project name
        :param int build_id:
        :param str continuation_token:
        :param int top: The maximum number of changes to return
        :param bool include_source_change:
        :rtype: [Change]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        query_parameters = {}
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if include_source_change is not None:
            query_parameters['includeSourceChange'] = self._serialize.query('include_source_change', include_source_change, 'bool')
        response = self._send(http_method='GET',
                              location_id='54572c7b-bbd3-45d4-80dc-28be08941620',
                              version='4.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[Change]', self._unwrap_collection(response))

    def get_build_controller(self, controller_id):
        """GetBuildController.
        Gets a controller
        :param int controller_id:
        :rtype: :class:`<BuildController> <azure.devops.v4_1.build.models.BuildController>`
        """
        route_values = {}
        if controller_id is not None:
            route_values['controllerId'] = self._serialize.url('controller_id', controller_id, 'int')
        response = self._send(http_method='GET',
                              location_id='fcac1932-2ee1-437f-9b6f-7f696be858f6',
                              version='4.1',
                              route_values=route_values)
        return self._deserialize('BuildController', response)

    def get_build_controllers(self, name=None):
        """GetBuildControllers.
        Gets controller, optionally filtered by name
        :param str name:
        :rtype: [BuildController]
        """
        query_parameters = {}
        if name is not None:
            query_parameters['name'] = self._serialize.query('name', name, 'str')
        response = self._send(http_method='GET',
                              location_id='fcac1932-2ee1-437f-9b6f-7f696be858f6',
                              version='4.1',
                              query_parameters=query_parameters)
        return self._deserialize('[BuildController]', self._unwrap_collection(response))

    def create_definition(self, definition, project=None, definition_to_clone_id=None, definition_to_clone_revision=None):
        """CreateDefinition.
        Creates a new definition.
        :param :class:`<BuildDefinition> <azure.devops.v4_1.build.models.BuildDefinition>` definition: The definition.
        :param str project: Project ID or project name
        :param int definition_to_clone_id:
        :param int definition_to_clone_revision:
        :rtype: :class:`<BuildDefinition> <azure.devops.v4_1.build.models.BuildDefinition>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if definition_to_clone_id is not None:
            query_parameters['definitionToCloneId'] = self._serialize.query('definition_to_clone_id', definition_to_clone_id, 'int')
        if definition_to_clone_revision is not None:
            query_parameters['definitionToCloneRevision'] = self._serialize.query('definition_to_clone_revision', definition_to_clone_revision, 'int')
        content = self._serialize.body(definition, 'BuildDefinition')
        response = self._send(http_method='POST',
                              location_id='dbeaf647-6167-421a-bda9-c9327b25e2e6',
                              version='4.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('BuildDefinition', response)

    def delete_definition(self, definition_id, project=None):
        """DeleteDefinition.
        Deletes a definition and all associated builds.
        :param int definition_id: The ID of the definition.
        :param str project: Project ID or project name
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if definition_id is not None:
            route_values['definitionId'] = self._serialize.url('definition_id', definition_id, 'int')
        self._send(http_method='DELETE',
                   location_id='dbeaf647-6167-421a-bda9-c9327b25e2e6',
                   version='4.1',
                   route_values=route_values)

    def get_definition(self, definition_id, project=None, revision=None, min_metrics_time=None, property_filters=None, include_latest_builds=None):
        """GetDefinition.
        Gets a definition, optionally at a specific revision.
        :param int definition_id: The ID of the definition.
        :param str project: Project ID or project name
        :param int revision: The revision number to retrieve. If this is not specified, the latest version will be returned.
        :param datetime min_metrics_time: If specified, indicates the date from which metrics should be included.
        :param [str] property_filters: A comma-delimited list of properties to include in the results.
        :param bool include_latest_builds:
        :rtype: :class:`<BuildDefinition> <azure.devops.v4_1.build.models.BuildDefinition>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if definition_id is not None:
            route_values['definitionId'] = self._serialize.url('definition_id', definition_id, 'int')
        query_parameters = {}
        if revision is not None:
            query_parameters['revision'] = self._serialize.query('revision', revision, 'int')
        if min_metrics_time is not None:
            query_parameters['minMetricsTime'] = self._serialize.query('min_metrics_time', min_metrics_time, 'iso-8601')
        if property_filters is not None:
            property_filters = ",".join(property_filters)
            query_parameters['propertyFilters'] = self._serialize.query('property_filters', property_filters, 'str')
        if include_latest_builds is not None:
            query_parameters['includeLatestBuilds'] = self._serialize.query('include_latest_builds', include_latest_builds, 'bool')
        response = self._send(http_method='GET',
                              location_id='dbeaf647-6167-421a-bda9-c9327b25e2e6',
                              version='4.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('BuildDefinition', response)

    def get_definitions(self, project=None, name=None, repository_id=None, repository_type=None, query_order=None, top=None, continuation_token=None, min_metrics_time=None, definition_ids=None, path=None, built_after=None, not_built_after=None, include_all_properties=None, include_latest_builds=None, task_id_filter=None):
        """GetDefinitions.
        Gets a list of definitions.
        :param str project: Project ID or project name
        :param str name: If specified, filters to definitions whose names match this pattern.
        :param str repository_id: A repository ID. If specified, filters to definitions that use this repository.
        :param str repository_type: If specified, filters to definitions that have a repository of this type.
        :param str query_order: Indicates the order in which definitions should be returned.
        :param int top: The maximum number of definitions to return.
        :param str continuation_token: A continuation token, returned by a previous call to this method, that can be used to return the next set of definitions.
        :param datetime min_metrics_time: If specified, indicates the date from which metrics should be included.
        :param [int] definition_ids: A comma-delimited list that specifies the IDs of definitions to retrieve.
        :param str path: If specified, filters to definitions under this folder.
        :param datetime built_after: If specified, filters to definitions that have builds after this date.
        :param datetime not_built_after: If specified, filters to definitions that do not have builds after this date.
        :param bool include_all_properties: Indicates whether the full definitions should be returned. By default, shallow representations of the definitions are returned.
        :param bool include_latest_builds: Indicates whether to return the latest and latest completed builds for this definition.
        :param str task_id_filter: If specified, filters to definitions that use the specified task.
        :rtype: [BuildDefinitionReference]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if name is not None:
            query_parameters['name'] = self._serialize.query('name', name, 'str')
        if repository_id is not None:
            query_parameters['repositoryId'] = self._serialize.query('repository_id', repository_id, 'str')
        if repository_type is not None:
            query_parameters['repositoryType'] = self._serialize.query('repository_type', repository_type, 'str')
        if query_order is not None:
            query_parameters['queryOrder'] = self._serialize.query('query_order', query_order, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if min_metrics_time is not None:
            query_parameters['minMetricsTime'] = self._serialize.query('min_metrics_time', min_metrics_time, 'iso-8601')
        if definition_ids is not None:
            definition_ids = ",".join(map(str, definition_ids))
            query_parameters['definitionIds'] = self._serialize.query('definition_ids', definition_ids, 'str')
        if path is not None:
            query_parameters['path'] = self._serialize.query('path', path, 'str')
        if built_after is not None:
            query_parameters['builtAfter'] = self._serialize.query('built_after', built_after, 'iso-8601')
        if not_built_after is not None:
            query_parameters['notBuiltAfter'] = self._serialize.query('not_built_after', not_built_after, 'iso-8601')
        if include_all_properties is not None:
            query_parameters['includeAllProperties'] = self._serialize.query('include_all_properties', include_all_properties, 'bool')
        if include_latest_builds is not None:
            query_parameters['includeLatestBuilds'] = self._serialize.query('include_latest_builds', include_latest_builds, 'bool')
        if task_id_filter is not None:
            query_parameters['taskIdFilter'] = self._serialize.query('task_id_filter', task_id_filter, 'str')
        response = self._send(http_method='GET',
                              location_id='dbeaf647-6167-421a-bda9-c9327b25e2e6',
                              version='4.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[BuildDefinitionReference]', self._unwrap_collection(response))

    def update_definition(self, definition, definition_id, project=None, secrets_source_definition_id=None, secrets_source_definition_revision=None):
        """UpdateDefinition.
        Updates an existing definition.
        :param :class:`<BuildDefinition> <azure.devops.v4_1.build.models.BuildDefinition>` definition: The new version of the defintion.
        :param int definition_id: The ID of the definition.
        :param str project: Project ID or project name
        :param int secrets_source_definition_id:
        :param int secrets_source_definition_revision:
        :rtype: :class:`<BuildDefinition> <azure.devops.v4_1.build.models.BuildDefinition>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if definition_id is not None:
            route_values['definitionId'] = self._serialize.url('definition_id', definition_id, 'int')
        query_parameters = {}
        if secrets_source_definition_id is not None:
            query_parameters['secretsSourceDefinitionId'] = self._serialize.query('secrets_source_definition_id', secrets_source_definition_id, 'int')
        if secrets_source_definition_revision is not None:
            query_parameters['secretsSourceDefinitionRevision'] = self._serialize.query('secrets_source_definition_revision', secrets_source_definition_revision, 'int')
        content = self._serialize.body(definition, 'BuildDefinition')
        response = self._send(http_method='PUT',
                              location_id='dbeaf647-6167-421a-bda9-c9327b25e2e6',
                              version='4.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('BuildDefinition', response)

    def get_build_log(self, project, build_id, log_id, start_line=None, end_line=None, **kwargs):
        """GetBuildLog.
        Gets an individual log file for a build.
        :param str project: Project ID or project name
        :param int build_id: The ID of the build.
        :param int log_id: The ID of the log file.
        :param long start_line: The start line.
        :param long end_line: The end line.
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        if log_id is not None:
            route_values['logId'] = self._serialize.url('log_id', log_id, 'int')
        query_parameters = {}
        if start_line is not None:
            query_parameters['startLine'] = self._serialize.query('start_line', start_line, 'long')
        if end_line is not None:
            query_parameters['endLine'] = self._serialize.query('end_line', end_line, 'long')
        response = self._send(http_method='GET',
                              location_id='35a80daf-7f30-45fc-86e8-6b813d9c90df',
                              version='4.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='text/plain')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_build_log_lines(self, project, build_id, log_id, start_line=None, end_line=None):
        """GetBuildLogLines.
        Gets an individual log file for a build.
        :param str project: Project ID or project name
        :param int build_id: The ID of the build.
        :param int log_id: The ID of the log file.
        :param long start_line: The start line.
        :param long end_line: The end line.
        :rtype: [str]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        if log_id is not None:
            route_values['logId'] = self._serialize.url('log_id', log_id, 'int')
        query_parameters = {}
        if start_line is not None:
            query_parameters['startLine'] = self._serialize.query('start_line', start_line, 'long')
        if end_line is not None:
            query_parameters['endLine'] = self._serialize.query('end_line', end_line, 'long')
        response = self._send(http_method='GET',
                              location_id='35a80daf-7f30-45fc-86e8-6b813d9c90df',
                              version='4.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[str]', self._unwrap_collection(response))

    def get_build_logs(self, project, build_id):
        """GetBuildLogs.
        Gets the logs for a build.
        :param str project: Project ID or project name
        :param int build_id: The ID of the build.
        :rtype: [BuildLog]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        response = self._send(http_method='GET',
                              location_id='35a80daf-7f30-45fc-86e8-6b813d9c90df',
                              version='4.1',
                              route_values=route_values)
        return self._deserialize('[BuildLog]', self._unwrap_collection(response))

    def get_build_logs_zip(self, project, build_id, **kwargs):
        """GetBuildLogsZip.
        Gets the logs for a build.
        :param str project: Project ID or project name
        :param int build_id: The ID of the build.
        :rtype: object
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        response = self._send(http_method='GET',
                              location_id='35a80daf-7f30-45fc-86e8-6b813d9c90df',
                              version='4.1',
                              route_values=route_values,
                              accept_media_type='application/zip')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_build_option_definitions(self, project=None):
        """GetBuildOptionDefinitions.
        Gets all build definition options supported by the system.
        :param str project: Project ID or project name
        :rtype: [BuildOptionDefinition]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        response = self._send(http_method='GET',
                              location_id='591cb5a4-2d46-4f3a-a697-5cd42b6bd332',
                              version='4.1',
                              route_values=route_values)
        return self._deserialize('[BuildOptionDefinition]', self._unwrap_collection(response))

    def get_definition_revisions(self, project, definition_id):
        """GetDefinitionRevisions.
        Gets all revisions of a definition.
        :param str project: Project ID or project name
        :param int definition_id: The ID of the definition.
        :rtype: [BuildDefinitionRevision]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if definition_id is not None:
            route_values['definitionId'] = self._serialize.url('definition_id', definition_id, 'int')
        response = self._send(http_method='GET',
                              location_id='7c116775-52e5-453e-8c5d-914d9762d8c4',
                              version='4.1',
                              route_values=route_values)
        return self._deserialize('[BuildDefinitionRevision]', self._unwrap_collection(response))

    def get_build_settings(self):
        """GetBuildSettings.
        Gets the build settings.
        :rtype: :class:`<BuildSettings> <azure.devops.v4_1.build.models.BuildSettings>`
        """
        response = self._send(http_method='GET',
                              location_id='aa8c1c9c-ef8b-474a-b8c4-785c7b191d0d',
                              version='4.1')
        return self._deserialize('BuildSettings', response)

    def update_build_settings(self, settings):
        """UpdateBuildSettings.
        Updates the build settings.
        :param :class:`<BuildSettings> <azure.devops.v4_1.build.models.BuildSettings>` settings: The new settings.
        :rtype: :class:`<BuildSettings> <azure.devops.v4_1.build.models.BuildSettings>`
        """
        content = self._serialize.body(settings, 'BuildSettings')
        response = self._send(http_method='PATCH',
                              location_id='aa8c1c9c-ef8b-474a-b8c4-785c7b191d0d',
                              version='4.1',
                              content=content)
        return self._deserialize('BuildSettings', response)

    def add_build_tag(self, project, build_id, tag):
        """AddBuildTag.
        Adds a tag to a build.
        :param str project: Project ID or project name
        :param int build_id: The ID of the build.
        :param str tag: The tag to add.
        :rtype: [str]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        if tag is not None:
            route_values['tag'] = self._serialize.url('tag', tag, 'str')
        response = self._send(http_method='PUT',
                              location_id='6e6114b2-8161-44c8-8f6c-c5505782427f',
                              version='4.1',
                              route_values=route_values)
        return self._deserialize('[str]', self._unwrap_collection(response))

    def add_build_tags(self, tags, project, build_id):
        """AddBuildTags.
        Adds tags to a build.
        :param [str] tags: The tags to add.
        :param str project: Project ID or project name
        :param int build_id: The ID of the build.
        :rtype: [str]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        content = self._serialize.body(tags, '[str]')
        response = self._send(http_method='POST',
                              location_id='6e6114b2-8161-44c8-8f6c-c5505782427f',
                              version='4.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[str]', self._unwrap_collection(response))

    def delete_build_tag(self, project, build_id, tag):
        """DeleteBuildTag.
        Removes a tag from a build.
        :param str project: Project ID or project name
        :param int build_id: The ID of the build.
        :param str tag: The tag to remove.
        :rtype: [str]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        if tag is not None:
            route_values['tag'] = self._serialize.url('tag', tag, 'str')
        response = self._send(http_method='DELETE',
                              location_id='6e6114b2-8161-44c8-8f6c-c5505782427f',
                              version='4.1',
                              route_values=route_values)
        return self._deserialize('[str]', self._unwrap_collection(response))

    def get_build_tags(self, project, build_id):
        """GetBuildTags.
        Gets the tags for a build.
        :param str project: Project ID or project name
        :param int build_id: The ID of the build.
        :rtype: [str]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        response = self._send(http_method='GET',
                              location_id='6e6114b2-8161-44c8-8f6c-c5505782427f',
                              version='4.1',
                              route_values=route_values)
        return self._deserialize('[str]', self._unwrap_collection(response))

    def get_tags(self, project):
        """GetTags.
        Gets a list of all build and definition tags in the project.
        :param str project: Project ID or project name
        :rtype: [str]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        response = self._send(http_method='GET',
                              location_id='d84ac5c6-edc7-43d5-adc9-1b34be5dea09',
                              version='4.1',
                              route_values=route_values)
        return self._deserialize('[str]', self._unwrap_collection(response))

    def delete_template(self, project, template_id):
        """DeleteTemplate.
        Deletes a build definition template.
        :param str project: Project ID or project name
        :param str template_id: The ID of the template.
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if template_id is not None:
            route_values['templateId'] = self._serialize.url('template_id', template_id, 'str')
        self._send(http_method='DELETE',
                   location_id='e884571e-7f92-4d6a-9274-3f5649900835',
                   version='4.1',
                   route_values=route_values)

    def get_template(self, project, template_id):
        """GetTemplate.
        Gets a specific build definition template.
        :param str project: Project ID or project name
        :param str template_id: The ID of the requested template.
        :rtype: :class:`<BuildDefinitionTemplate> <azure.devops.v4_1.build.models.BuildDefinitionTemplate>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if template_id is not None:
            route_values['templateId'] = self._serialize.url('template_id', template_id, 'str')
        response = self._send(http_method='GET',
                              location_id='e884571e-7f92-4d6a-9274-3f5649900835',
                              version='4.1',
                              route_values=route_values)
        return self._deserialize('BuildDefinitionTemplate', response)

    def get_templates(self, project):
        """GetTemplates.
        Gets all definition templates.
        :param str project: Project ID or project name
        :rtype: [BuildDefinitionTemplate]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        response = self._send(http_method='GET',
                              location_id='e884571e-7f92-4d6a-9274-3f5649900835',
                              version='4.1',
                              route_values=route_values)
        return self._deserialize('[BuildDefinitionTemplate]', self._unwrap_collection(response))

    def save_template(self, template, project, template_id):
        """SaveTemplate.
        Updates an existing build definition template.
        :param :class:`<BuildDefinitionTemplate> <azure.devops.v4_1.build.models.BuildDefinitionTemplate>` template: The new version of the template.
        :param str project: Project ID or project name
        :param str template_id: The ID of the template.
        :rtype: :class:`<BuildDefinitionTemplate> <azure.devops.v4_1.build.models.BuildDefinitionTemplate>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if template_id is not None:
            route_values['templateId'] = self._serialize.url('template_id', template_id, 'str')
        content = self._serialize.body(template, 'BuildDefinitionTemplate')
        response = self._send(http_method='PUT',
                              location_id='e884571e-7f92-4d6a-9274-3f5649900835',
                              version='4.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('BuildDefinitionTemplate', response)

    def get_build_timeline(self, project, build_id, timeline_id=None, change_id=None, plan_id=None):
        """GetBuildTimeline.
        Gets details for a build
        :param str project: Project ID or project name
        :param int build_id:
        :param str timeline_id:
        :param int change_id:
        :param str plan_id:
        :rtype: :class:`<Timeline> <azure.devops.v4_1.build.models.Timeline>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        if timeline_id is not None:
            route_values['timelineId'] = self._serialize.url('timeline_id', timeline_id, 'str')
        query_parameters = {}
        if change_id is not None:
            query_parameters['changeId'] = self._serialize.query('change_id', change_id, 'int')
        if plan_id is not None:
            query_parameters['planId'] = self._serialize.query('plan_id', plan_id, 'str')
        response = self._send(http_method='GET',
                              location_id='8baac422-4c6e-4de5-8532-db96d92acffa',
                              version='4.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('Timeline', response)

    def get_build_work_items_refs(self, project, build_id, top=None):
        """GetBuildWorkItemsRefs.
        Gets the work items associated with a build.
        :param str project: Project ID or project name
        :param int build_id: The ID of the build.
        :param int top: The maximum number of work items to return.
        :rtype: [ResourceRef]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        query_parameters = {}
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        response = self._send(http_method='GET',
                              location_id='5a21f5d2-5642-47e4-a0bd-1356e6731bee',
                              version='4.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[ResourceRef]', self._unwrap_collection(response))

    def get_build_work_items_refs_from_commits(self, commit_ids, project, build_id, top=None):
        """GetBuildWorkItemsRefsFromCommits.
        Gets the work items associated with a build, filtered to specific commits.
        :param [str] commit_ids: A comma-delimited list of commit IDs.
        :param str project: Project ID or project name
        :param int build_id: The ID of the build.
        :param int top: The maximum number of work items to return, or the number of commits to consider if no commit IDs are specified.
        :rtype: [ResourceRef]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if build_id is not None:
            route_values['buildId'] = self._serialize.url('build_id', build_id, 'int')
        query_parameters = {}
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        content = self._serialize.body(commit_ids, '[str]')
        response = self._send(http_method='POST',
                              location_id='5a21f5d2-5642-47e4-a0bd-1356e6731bee',
                              version='4.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('[ResourceRef]', self._unwrap_collection(response))
